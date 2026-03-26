from pydantic import BaseModel
from app.schemas.predict import PredictResponse


class CopilotRequest(BaseModel):
    question: str
    explanation_payload: PredictResponse


class CopilotResponse(BaseModel):
    summary: str
    model_rationale: str
    evidence: list[str]
    citations: list[str]
    limitations: str
    uncertainty: str