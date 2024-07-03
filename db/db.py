from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.pool import NullPool
import os
from dotenv import load_dotenv

load_dotenv()

POSTGRES_NAME = os.getenv("POSTGRES_NAME")
DB_PASS = os.getenv('DB_PASS')
LOCALHOST = os.getenv('LOCALHOST')
DB_NAME = os.getenv('DB_NAME')


engine = create_async_engine(f"postgresql+asyncpg://{POSTGRES_NAME}:{DB_PASS}@{LOCALHOST}/{DB_NAME}",
                             poolclass = NullPool)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


class Base(DeclarativeBase):
    pass
#

async def get_async_session():
    async with async_session_maker() as session:
        yield session


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def delete_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
