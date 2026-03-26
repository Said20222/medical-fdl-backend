def get_seed_documents():
    return [
        {
            "id": "rule_r1",
            "text": (
                "Rule R1: If tumor size is high and enhancement pattern is suspicious, "
                "the model increases likelihood of kidney cancer presence."
            ),
            "metadata": {
                "source": "rulebook",
                "title": "Fuzzy Rule R1",
                "chunk_id": "rule_r1_chunk_1"
            },
        },
        {
            "id": "rule_r7",
            "text": (
                "Rule R7: If imaging evidence is moderate but clinical risk factors are present, "
                "the model may still classify the case as present with moderate strength."
            ),
            "metadata": {
                "source": "rulebook",
                "title": "Fuzzy Rule R7",
                "chunk_id": "rule_r7_chunk_1"
            },
        },
        {
            "id": "feature_tumor_size",
            "text": (
                "Feature dictionary: tumor_size_cm represents the maximum tumor diameter in centimeters. "
                "Larger tumor size is often associated with elevated malignancy risk."
            ),
            "metadata": {
                "source": "feature_dictionary",
                "title": "Tumor Size Feature",
                "chunk_id": "feature_tumor_size_chunk_1"
            },
        },
        {
            "id": "feature_age",
            "text": (
                "Feature dictionary: age is the patient's age in years. Age may contribute to risk estimation "
                "but should not be interpreted in isolation."
            ),
            "metadata": {
                "source": "feature_dictionary",
                "title": "Age Feature",
                "chunk_id": "feature_age_chunk_1"
            },
        },
        {
            "id": "guideline_1",
            "text": (
                "Guideline excerpt: Imaging findings should be interpreted together with clinical context. "
                "No single feature should be treated as definitive evidence without corroboration."
            ),
            "metadata": {
                "source": "guideline_excerpt",
                "title": "Clinical Interpretation Note",
                "chunk_id": "guideline_1_chunk_1"
            },
        },
    ]