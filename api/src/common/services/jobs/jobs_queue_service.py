import aio_pika
import logging
import json
from src.common.entities.job_entity import JobEntity
from fastapi.encoders import jsonable_encoder
from settings import RABBITMQ_HOST, RABBITMQ_PORT

JOBS_QUEUE_NAME = 'jobs_queue'


class _JobsQueueService:
    def __init__(self):
        self.connection = None
        self.channel = None
        self.jobs_queue = None

    async def start(self):
        self.connection = await aio_pika.connect_robust(
            host=RABBITMQ_HOST,
            port=int(RABBITMQ_PORT)
        )
        self.channel = await self.connection.channel()
        self.jobs_queue = await self.channel.declare_queue(JOBS_QUEUE_NAME, durable=True)
        logging.info("JobsQueueService started")

    async def queue_job(self, job: JobEntity):
        body = json.dumps(jsonable_encoder(job)).encode()
        await self.channel.default_exchange.publish(
            aio_pika.Message(body),
            routing_key=self.jobs_queue.name,
        )

    async def stop(self):
        await self.channel.close()
        await self.connection.close()
        logging.info("JobsQueueService stopped")


jobs_queue_service = _JobsQueueService()
