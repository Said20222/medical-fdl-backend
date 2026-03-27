from app.schemas.predict import PredictRequest


class ModelAdapter:
    def __init__(self):
        self.model = self._load_model()

    def _load_model(self):
        """
        Temporary placeholder for real model loading.
        Later this can load:
        - a checkpoint
        - a Python model object
        - a wrapped inference pipeline
        """
        return None

    def _prepare_input(self, payload: PredictRequest):
        """
        Temporary placeholder for input preprocessing.
        Later this will convert the FastAPI request into
        the format expected by the fuzzy-DL model.
        """
        return {
            "age": payload.age,
            "tumor_size_cm": payload.tumor_size_cm,
            "imaging_modality": payload.imaging_modality,
        }

    def run_inference(self, payload: PredictRequest) -> dict:
        model_input = self._prepare_input(payload)

        # Temporary stubbed output until the real model is connected
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
            "debug_model_input": model_input,
        }