import asyncio

from dispatcher.DispatcherWindows import DispatcherWindows
from repository.metrics_repository import MetricsRepository
from services.metrics import MetricsService


async def db_write_metrics(dispatcher: DispatcherWindows = DispatcherWindows()):
    print("ASDASG")
    service = MetricsService(MetricsRepository)
    data = await dispatcher.form_metrics()
    await service.add_one(data)
    await asyncio.sleep(3)


async def prepare() -> None:
    dispatcher = DispatcherWindows()
    # await db_write_general_data(dispatcher)
    while True:
        await db_write_metrics(dispatcher)


def main() -> None:
    asyncio.run(prepare())