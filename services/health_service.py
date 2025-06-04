from repositories.health_repository import HealthRepository
from fastapi import HTTPException

class HealthService:
    @staticmethod
    async def update_health(user_id: str, data: dict):
        updated = await HealthRepository.update_health_data(user_id, data)
        if not updated:
            raise HTTPException(status_code=404, detail="User not found")
        return updated

    @staticmethod
    async def get_health(user_id: str):
        data = await HealthRepository.get_health_data(user_id)
        if not data:
            raise HTTPException(status_code=404, detail="Health data not found")
        return data
