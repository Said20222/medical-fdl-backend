from pydantic import BaseModel, Field
from typing import Optional


class TopFeature(BaseModel):
    name: str
    weight: float


class FiredRule(BaseModel):
    id: str
    description: str
    strength: Optional[float] = None

# gotta work on this later, just a placeholder for now
class PredictRequest(BaseModel):
    age: int = Field(..., example=58)
    tumor_size_cm: float = Field(..., example=4.2)
    imaging_modality: str = Field(..., example="CT")


class PredictResponse(BaseModel):
    prediction: int
    confidence: float
    top_features: list[TopFeature]
    fired_rules: list[FiredRule]