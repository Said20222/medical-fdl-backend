from app.services.chroma_store import ChromaStore
from app.services.llm_client import LLMClient


class CopilotService:
    def __init__(self):
        self.store = ChromaStore()
        self.llm = LLMClient()

    def _should_abstain(self, explanation_payload: dict, retrieved: list[dict]) -> tuple[bool, str]:
        if not retrieved:
            return True, "No documents were retrieved from the knowledge base."

        top_features = explanation_payload.get("top_features", [])
        fired_rules = explanation_payload.get("fired_rules", [])

        feature_names = [feature["name"].lower() for feature in top_features]
        rule_ids = [rule["id"].lower() for rule in fired_rules]

        retrieved_text = " ".join(item["text"].lower() for item in retrieved)

        feature_match = any(name in retrieved_text for name in feature_names)
        rule_match = any(rule_id in retrieved_text for rule_id in rule_ids)

        if not feature_match and not rule_match:
            return True, (
                "Retrieved documents do not align well with the model's top features "
                "or fired rules."
            )

        return False, ""
    
    def _build_retrieval_query(self, question: str, explanation_payload: dict) -> str:
        top_features = explanation_payload.get("top_features", [])
        fired_rules = explanation_payload.get("fired_rules", [])

        feature_names = [feature["name"] for feature in top_features]
        rule_ids = [rule["id"] for rule in fired_rules]

        parts = [question] + feature_names + rule_ids
        return " ".join(parts)

    def generate_answer(self, question: str, explanation_payload: dict):
        self.store.seed_if_empty()
        retrieval_query = self._build_retrieval_query(question, explanation_payload)
        retrieved = self.store.query(question=retrieval_query, k=3)

        should_abstain, reason = self._should_abstain(
            explanation_payload=explanation_payload,
            retrieved=retrieved,
        )

        if should_abstain:
            abstention_response = {
                "summary": "I do not have enough grounded evidence to answer confidently.",
                "model_rationale": (
                    "The current retrieved documents do not align strongly enough with the "
                    "model's explanation payload."
                ),
                "evidence": [],
                "citations": [],
                "limitations": reason,
                "uncertainty": (
                    "The available corpus may be incomplete or not sufficiently relevant "
                    "to this question."
                ),
            }
            import json
            return json.dumps(abstention_response), retrieved

        context_text = "\n\n".join(
            [f"[{item['id']}] {item['text']}" for item in retrieved]
        )

        system_prompt = (
            "You are a medical AI assistant. "
            "You must answer ONLY using the provided context and model explanation. "
            "If the context is insufficient, say you are uncertain."
        )

        user_prompt = f"""
Question:
{question}

Model Output:
{explanation_payload}

Retrieved Context:
{context_text}

Instructions:
- Answer ONLY using the model output and retrieved context.
- If the context is insufficient, say so clearly.
- Return valid JSON only.
- Do not include markdown fences.
- "summary" must be a short string.
- "model_rationale" must be a short string.
- "evidence" must be a list of short bullet strings.
- "citations" must be a list of source IDs like ["rule_r1", "feature_tumor_size"].
- "limitations" must be a short string.
- "uncertainty" must be a short string.

Return this exact JSON shape:
{{
  "summary": "string",
  "model_rationale": "string",
  "evidence": ["string", "string"],
  "citations": ["string", "string"],
  "limitations": "string",
  "uncertainty": "string"
}}
"""

        raw_response = self.llm.chat(system_prompt, user_prompt)
        return raw_response, retrieved