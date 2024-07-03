from abc import ABC, abstractmethod

from sqlalchemy import insert, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from db.db import async_session_maker


class AbstractRepo(ABC):
    @abstractmethod
    async def add_one(self, data: dict):
        raise NotImplementedError

    @abstractmethod
    async def get_all(self):
        raise NotImplementedError



class SQLAlchemyRepo(AbstractRepo):
    model = None

    async def add_one(self, data: dict) -> int:
        async with async_session_maker() as session:
            statement = insert(self.model).values(**data).returning(self.model.id)
            res = await session.execute(statement)
            await session.commit()
            return res.scalar_one()

    async def get_all(self):
        async with async_session_maker() as session:
            statement = select(self.model)
            res = await session.execute(statement)
            res = [row[0] for row in res]
            return res

    async def get_all_limit(self, limit:int = None):
        """
        return last N rows
        :param limit:
        :return:
        """
        async with async_session_maker() as session:
            statement = select(self.model).order_by(self.model.id.desc()).limit(limit)
            res = await session.execute(statement)
            res = [row[0] for row in res]
            return res