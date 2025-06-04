from core.database import DATABASE
from typing import Optional

class HealthRepository:
    @staticmethod
    async def update_health_data(user_id: str, data: dict) -> dict:
        await DATABASE['health_data'].update_one({'user_id': user_id}, {'$set': data}, upsert=True)
        return await DATABASE['health_data'].find_one({'user_id': user_id})

    @staticmethod
    async def get_health_data(user_id: str) -> Optional[dict]:
        return await DATABASE['health_data'].find_one({'user_id': user_id})
