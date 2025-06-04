from typing import Optional
from bson import ObjectId

class UserRepository:
    def __init__(self, collection):
        self.collection = collection

    async def create_user(self, user_data: dict) -> str:
        res = await self.collection.insert_one(user_data)
        return str(res.inserted_id)

    async def get_user(self, user_id: str) -> Optional[dict]:
        user = await self.collection.find_one({"_id": ObjectId(user_id)})
        if user:
            user["id"] = str(user["_id"])
            return user
        return None

    async def update_user_health(self, user_id: str, health_data: dict) -> bool:
        update_result = await self.collection.update_one(
            {"_id": ObjectId(user_id)},
            {"$set": health_data}
        )
        return update_result.modified_count > 0
