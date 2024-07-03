from typing import Type
from utils.abstactrepo import AbstractRepo, SQLAlchemyRepo


class MetricsService:
    def __init__(self, repository:  Type[SQLAlchemyRepo]):
        self.repository = repository()

    async def add_one(self, data):
        metrics = await self.repository.add_one(data)
        return metrics

    async def get_all_metrics(self):
        metrics = await self.repository.get_all()
        return metrics

    async def get_limit_metrics(self, limit: int = None):
        metrics = await self.repository.get_all_limit(limit)
        return metrics
