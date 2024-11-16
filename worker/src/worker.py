
import logging
import aio_pika
import lasio
from src.plots.factory.factory import Factory
from src.utils.dataframe import filter_by_index
from .job import Job

# TODO: extract these into env vars
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
        self.multiplot = Factory.make_multiplot()

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
        
    def read_las_file(self, job):
        # TO-DO: Dont know why it doesnt work with STORAGE_PATH (Check this)
        file_path = f"./static/{job.well_id}/{job.parameters["filename"]}"
        dataframe = lasio.read(file_path).df()
        
        if job.parameters.get("min_window") and job.parameters.get("max_window"):
            dataframe = filter_by_index(dataframe, job.parameters["min_window"], job.parameters["max_window"])
        
        return dataframe

    def write_csv(self, dataframe, path):
        numeric_dataframe = dataframe.select_dtypes(include=['number'])
        variation = numeric_dataframe.diff().abs().sum(axis=1)
        representative_dataframe = dataframe.loc[variation.nlargest(200).index]
        representative_dataframe.to_csv(path)
        return {"csv": path}
    
    async def process_message(self, message):
        job = Job.model_validate_json(message.body.decode())
        logging.info(f"Processing job: {job}")

        try:
            dataframe = self.read_las_file(job)                                
            images = self.multiplot.plot(dataframe, f"./static/{job.well_id}/{job.id}/graphs")
                        
            if job.type == 'NEW_WELL':
                job.result = self.write_csv(dataframe[['GR']], f"./static/{job.well_id}/gamma_ray.csv")
            
            job.result = {**job.result, "graphs": images}
            job.status = "processed"
        except Exception as e:
            logging.error(f"Failed to process job {job.id}: {e}")
            job.status = "failed"
        finally:
            await self.channel.default_exchange.publish(
                aio_pika.Message(body=job.model_dump_json().encode()),
                routing_key=self.output_queue.name,
            )
