
import logging
import aio_pika

RABBITMQ_HOST = "rabbitmq"
RABBITMQ_PORT = "5672"


class Worker:
    def __init__(self, input_queue_name, output_queue_name):
        self.input_queue_name = input_queue_name
        self.output_queue_name = output_queue_name
        self.connection = None
        self.channel = None
        self.input_queue = None
        self.output_queue = None

    async def start(self):
        self.connection = await aio_pika.connect_robust(
            host=RABBITMQ_HOST,
            port=int(RABBITMQ_PORT)
        )
        self.channel = await self.connection.channel()
        await self.channel.set_qos(prefetch_count=1)

        self.input_queue = await self.channel.declare_queue(self.input_queue_name, durable=True)
        self.output_queue = await self.channel.declare_queue(self.output_queue_name, durable=True)

        logging.info(f"Worker started. Consuming messages from queue: {self.input_queue.name}")
        async with self.input_queue.iterator() as queue_iter:
            async for message in queue_iter:
                async with message.process():
                    await self.process_message(message)

    async def stop(self):
        await self.channel.close()
        await self.connection.close()
        logging.info("Worker stopped")

    async def process_message(self, message):
        # TODO: Implement processing of jobs
        logging.info(message.body)

        result = message.body
        # Publish the result to the output queue
        await self.channel.default_exchange.publish(
            aio_pika.Message(body=result),
            routing_key=self.output_queue.name,
        )
