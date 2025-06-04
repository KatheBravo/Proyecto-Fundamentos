from fastapi import HTTPException
from typing import Optional
from models.user import UserBase, UserCreate, UserInDB, UserUpdateHealth
from repositories.user_repository import UserRepository

class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    async def register_user(self, user_create: UserCreate) -> UserInDB:
        user_dict = user_create.dict()
        user_dict["programa"] = self.asignar_programa(user_create)
        user_id = await self.repository.create_user(user_dict)
        user_dict["id"] = user_id
        return UserInDB(**user_dict)

    def asignar_programa(self, user: UserBase) -> str:
        if user.tiene_condiciones_medicas:
            return "Programa Suave"
        elif user.edad > 60:
            return "Programa para Adultos Mayores"
        elif user.peso / ((user.altura / 100) ** 2) > 25:
            return "Programa de Pérdida de Peso"
        else:
            return "Programa General"

    async def obtener_programa(self, user_id: str) -> str:
        user = await self.repository.get_user(user_id)
        if not user:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        return user.get("programa", "No asignado")

    async def actualizar_salud(self, user_id: str, health_update: UserUpdateHealth) -> UserInDB:
        update_data = health_update.dict(exclude_unset=True)
        if "tiene_condiciones_medicas" in update_data and update_data["tiene_condiciones_medicas"] and not update_data.get("condicion_medica"):
            raise HTTPException(status_code=400, detail="Debe especificar la condición médica si tiene condiciones.")
        
        updated = await self.repository.update_user_health(user_id, update_data)
        if not updated:
            raise HTTPException(status_code=404, detail="Usuario no encontrado o sin cambios")

        user = await self.repository.get_user(user_id)
        programa_nuevo = self.asignar_programa(UserBase(**user))
        if programa_nuevo != user.get("programa"):
            await self.repository.update_user_health(user_id, {"programa": programa_nuevo})
            user["programa"] = programa_nuevo

        return UserInDB(**user)
