import logging
import signal
import asyncio
from src.worker import Worker

logging.basicConfig(
    format="%(asctime)s [%(levelname)s]: %(message)s",
    level='INFO'
)


async def main():
    input_queue = "jobs_queue"
    output_queue = "results_queue"
    worker = Worker(input_queue, output_queue)
    signal.signal(signal.SIGTERM, lambda signum, frame: asyncio.create_task(worker.stop()))
    await worker.start()


if __name__ == "__main__":
    asyncio.run(main())
