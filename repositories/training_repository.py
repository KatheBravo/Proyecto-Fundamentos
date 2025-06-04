from core.database import DATABASE
from typing import List

class TrainingRepository:
    @staticmethod
    async def get_training_programs(user_id: str, goal: str = None) -> List[dict]:
        query = {'user_id': user_id}
        if goal:
            query['goal'] = goal
        cursor = DATABASE['training_programs'].find(query)
        return [{**doc, 'id': str(doc['_id'])} async for doc in cursor]
