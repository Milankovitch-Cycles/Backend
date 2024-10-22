import aio_pika
import logging
from settings import RABBITMQ_HOST, RABBITMQ_PORT

RESULTS_QUEUE_NAME = 'results_queue'


class _JobsResultsConsumer:
    def __init__(self):
        self.connection = None
        self.channel = None
        self.results_queue = None

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
        # TODO: Implement processing of results
        logging.info(message.body)


jobs_results_consumer = _JobsResultsConsumer()
