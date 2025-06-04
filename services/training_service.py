from repositories.training_repository import TrainingRepository

class TrainingService:
    @staticmethod
    async def get_programs(user_id: str, goal: str = None):
        return await TrainingRepository.get_training_programs(user_id, goal)
