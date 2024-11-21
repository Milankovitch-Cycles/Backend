import aio_pika
import logging
import json
from src.modules.wells.well_service import WellService
from src.common.services.smtp.smtp_service import SmtpService
from src.modules.users.user_service import UserService
from settings import RABBITMQ_HOST, RABBITMQ_PORT

RESULTS_QUEUE_NAME = 'results_queue'


class _JobsResultsConsumer:
    def __init__(self):
        self.connection = None
        self.channel = None
        self.results_queue = None
        self.smtp_service = SmtpService()
        self.user_service = UserService()
        self.well_service = WellService()

    async def start(self):
        self.connection = await aio_pika.connect_robust(
            host=RABBITMQ_HOST,
            port=int(RABBITMQ_PORT)
        )
        self.channel = await self.connection.channel()
        await self.channel.set_qos(prefetch_count=1)

        self.results_queue = await self.channel.declare_queue(RESULTS_QUEUE_NAME, durable=True)

        logging.info(f"JobsResultsConsumer started. Consuming results from queue: {self.results_queue.name}")
        async with self.results_queue.iterator() as queue_iter:
            async for message in queue_iter:
                async with message.process():
                    self.process_message(message)

    async def stop(self):
        await self.channel.close()
        await self.connection.close()
        logging.info("JobsResultsConsumer stopped")

    def process_message(self, message):
        decode_message = json.loads(message.body.decode())
        logging.info(f"Decoded message: {decode_message}")
        user = self.user_service.get_by_id(decode_message["user_id"])
        self.well_service.update_job(decode_message["id"], {"status": decode_message["status"], "result": decode_message["result"]}, user)
        self.smtp_service.send_email(
            receiver=user.email,
            title="Job completed 🤝",
            text="Your job has been completed 🛢️ 🌍"
        )

jobs_results_consumer = _JobsResultsConsumer()
