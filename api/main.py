import asyncio
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from src.modules.auth.auth_routes import auth
from src.modules.wells.well_routes import wells
from src.common.services.jobs.jobs_results_consumer import jobs_results_consumer
from src.common.services.jobs.jobs_queue_service import jobs_queue_service
from src.common.config.logging_config import setup_logging
from fastapi.staticfiles import StaticFiles
import os
import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    setup_logging()
    # Start the jobs results service and consumer
    tasks = [asyncio.create_task(jobs_queue_service.start()),
             asyncio.create_task(jobs_results_consumer.start())]
    yield
    # Stop the jobs results service and consumer
    await jobs_queue_service.stop()
    await jobs_results_consumer.stop()
    for task in tasks:
        task.cancel()


app = FastAPI(title="Milankovic API", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth)
app.include_router(wells)

app.mount("/static", StaticFiles(directory=os.path.dirname(__file__)+'/'+settings.STORAGE_PATH), name="static")
