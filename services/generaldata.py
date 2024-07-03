from typing import Type
from utils.abstactrepo import AbstractRepo
# from schemas.task import AddTaskSchema


class GeneralDataService:
    def __init__(self, repository:  Type[AbstractRepo]):
        self.repository = repository()

    async def add_one(self, data):
        # task_dict = task.model_dump()
        task_id = await self.repository.add_one(data)
        return task_id

    async def get_all(self):
        general = await self.repository.get_all()
        return general