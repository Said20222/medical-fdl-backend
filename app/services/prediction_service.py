from app.schemas.predict import PredictRequest, PredictResponse
from app.services.model_adapter import ModelAdapter


class PredictionService:
    def __init__(self):
        self.model_adapter = ModelAdapter()

    def predict(self, payload: PredictRequest) -> PredictResponse:
        raw_output = self.model_adapter.run_inference(payload)

        return PredictResponse(
            prediction=raw_output["prediction"],
            confidence=raw_output["confidence"],
            top_features=raw_output["top_features"],
            fired_rules=raw_output["fired_rules"],
        )