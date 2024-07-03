import asyncio

from dispatcher.DispatcherWindows import DispatcherWindows
from repository.generaldata_repository import GeneralDataRepository
from repository.metrics_repository import MetricsRepository
from services.generaldata import GeneralDataService
from services.metrics import MetricsService


async def db_write_general_data(dispatcher: DispatcherWindows):
    service = GeneralDataService(GeneralDataRepository)
    data = await dispatcher.form_general_data()
    await service.add_one(data)


async def prepare_general():
    dispatcher = DispatcherWindows()
    await db_write_general_data(dispatcher)
    # while True:
    #     await db_write_metrics(dispatcher)
    #     await asyncio.sleep(3)


# asyncio.run(main())