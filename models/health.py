from pydantic import BaseModel
from typing import Optional

class HealthDataUpdate(BaseModel):
    user_id: str
    height_cm: Optional[float] = None
    weight_kg: Optional[float] = None
    heart_rate: Optional[int] = None

class HealthDataResponse(BaseModel):
    user_id: str
    height_cm: Optional[float]
    weight_kg: Optional[float]
    heart_rate: Optional[int]
