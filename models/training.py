from pydantic import BaseModel
from typing import List, Optional

class TrainingQuery(BaseModel):
    user_id: str
    goal: Optional[str] = None

class TrainingProgram(BaseModel):
    id: str
    user_id: str
    exercises: List[str]
    goal: Optional[str] = None
