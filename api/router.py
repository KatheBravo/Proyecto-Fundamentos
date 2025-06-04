from fastapi import APIRouter, Depends, HTTPException
from models.user import UserCreate, UserInDB, UserUpdateHealth
from repositories.user_repository import UserRepository
from services.user_service import UserService
from core.database import get_user_collection

router = APIRouter()

def get_user_repository():
    collection = get_user_collection()
    return UserRepository(collection)

def get_user_service(repo: UserRepository = Depends(get_user_repository)):
    return UserService(repo)

@router.post("/usuarios/", response_model=UserInDB)
async def registrar_usuario(user: UserCreate, service: UserService = Depends(get_user_service)):
    try:
        return await service.register_user(user)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/usuarios/{user_id}/programa", response_model=str)
async def obtener_programa(user_id: str, service: UserService = Depends(get_user_service)):
    return await service.obtener_programa(user_id)

@router.patch("/usuarios/{user_id}/salud", response_model=UserInDB)
async def actualizar_datos_salud(user_id: str, health_update: UserUpdateHealth, service: UserService = Depends(get_user_service)):
    return await service.actualizar_salud(user_id, health_update)
