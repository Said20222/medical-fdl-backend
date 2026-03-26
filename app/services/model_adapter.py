from app.schemas.predict import PredictRequest


class ModelAdapter:
    def run_inference(self, payload: PredictRequest) -> dict:
        """
        Temporary stub for the real fuzzy-DL model.

        Later, this method will:
        - preprocess input
        - call the actual model
        - return raw model output
        """

        return {
            "prediction": 1,
            "confidence": 0.87,
            "top_features": [
                {"name": "tumor_size_cm", "weight": 0.42},
                {"name": "age", "weight": 0.21},
                {"name": "imaging_modality:CT", "weight": 0.15},
            ],
            "fired_rules": [
                {
                    "id": "R1",
                    "description": "If tumor size is high and enhancement pattern is suspicious, risk is elevated.",
                    "strength": 0.91,
                },
                {
                    "id": "R7",
                    "description": "If imaging evidence is moderate but clinical risk factors are present, classify as present.",
                    "strength": 0.63,
                },
            ],
        }