from pydantic import BaseModel, Field, validator
from typing import Optional

class UserBase(BaseModel):
    nombre: str = Field(..., min_length=2, max_length=50)
    edad: int = Field(..., gt=0, lt=120)
    peso: float = Field(..., gt=0)
    altura: float = Field(..., gt=0)
    tiene_condiciones_medicas: bool = False
    condicion_medica: Optional[str] = None

    @validator("condicion_medica")
    def validar_condicion_si_aplica(cls, v, values):
        if values.get('tiene_condiciones_medicas') and not v:
            raise ValueError("Debe especificar la condición médica si tiene condiciones.")
        return v

class UserCreate(UserBase):
    pass

class UserUpdateHealth(BaseModel):
    peso: Optional[float] = Field(None, gt=0)
    altura: Optional[float] = Field(None, gt=0)
    tiene_condiciones_medicas: Optional[bool]
    condicion_medica: Optional[str]

class UserInDB(UserBase):
    id: str
