import asyncio
import uvicorn
import multiprocessing

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from contextlib import asynccontextmanager

from api.routers import all_routers
from pages.router import router as pages_router

from dispatcher.utils.write_general import prepare_general
from dispatcher.utils.write_db import main, prepare, db_write_metrics
from db.db import delete_tables, create_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print('delete all tables')
    await create_tables()
    print('create tables')
    await prepare_general()
    # await prepare()
    yield


app = FastAPI(

    title='Simple metrics',
    lifespan=lifespan
)

for router in all_routers:
    app.include_router(router, prefix='/api')

app.include_router(pages_router)


app.mount('/static', StaticFiles(directory='static'), name='static')

origins = [
    "http://localhost",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def start_fastapi() -> None:
    uvicorn.run(app='main:app', reload=True)

def start_metrics(loop) -> None:
    loop.create_task(prepare())

if __name__ == "__main__":
    # loop = asyncio.new_event_loop()
    # asyncio.set_event_loop(loop)
    # start_metrics(loop)
    # start_fastapi(loop)
    process1 = multiprocessing.Process(target=main)
    process2 = multiprocessing.Process(target=start_fastapi)

    process1.start()
    process2.start()
    # uvicorn.run(app='main:app', reload=True)
