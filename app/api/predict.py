from fastapi import APIRouter
from app.schemas.predict import PredictRequest, PredictResponse
from app.services.prediction_service import PredictionService

router = APIRouter(prefix="/api", tags=["predict"])


@router.post("/predict", response_model=PredictResponse)
def predict(payload: PredictRequest):
    service = PredictionService()
    return service.predict(payload)