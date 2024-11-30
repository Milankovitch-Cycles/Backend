
import logging
import aio_pika
import lasio
import os
from src.plots.factory.factory import Factory
from src.utils.dataframe import filter_by_index
from src.fourier_transform import FourierTransform
from worker.src.milankovic_cycle_analyzer import MilankovitchCycleAnalyzer
from .job import Job
from pandas import DataFrame

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

    def write_csv(self, dataframe: DataFrame, path: str, type: str):
        if not os.path.exists(os.path.dirname(path)):
            os.makedirs(os.path.dirname(path))       
        if type == 'MILANKOVIC_CYCLES':
            dataframe.to_csv(path, float_format='%.6f', index=False)
        else:
            numeric_dataframe = dataframe.select_dtypes(include=['int'])
            variation = numeric_dataframe.diff().abs().sum(axis=1)
            representative_dataframe = dataframe.loc[variation.nlargest(200).index]
            representative_dataframe.to_csv(path, float_format='%.0f')
        return path
    
    async def process_message(self, message):
        job = Job.model_validate_json(message.body.decode())
        logging.info(f"Processing job: {job}")

        try:
            dataframe = self.read_las_file(job)                                
            
            if job.type in ["NEW_WELL", "GRAPHS"]:
                images = self.multiplot.plot(dataframe, f"./static/{job.well_id}/{job.id}/graphs")
                job.result = {**job.result, "graphs": images}

            if job.type == 'NEW_WELL':
                dataframe['TEMP_DEPTH'] = dataframe.index.astype(int)
                dataframe['GR'] = dataframe['GR'].dropna().astype(int)
                dataframe = dataframe.groupby('TEMP_DEPTH').mean()
                gamma_ray_path = self.write_csv(dataframe[['GR']], f"./static/{job.well_id}/gamma_ray.txt", type=job.type)
                job.result = {**job.result, "gamma_ray_path": gamma_ray_path}
            
            elif job.type == 'MILANKOVIC_CYCLES':
                frequency_dataframe = FourierTransform.convert_to_frequency_domain(dataframe, "GR", 0.001)
                frequency_path = f"./static/{job.well_id}/{job.id}/frequencies.txt"
                self.write_csv(frequency_dataframe, frequency_path, job.type)
                cycles = MilankovitchCycleAnalyzer.detect_cycles(frequency_dataframe)
                job.result = {**job.result, "frequencies_path": frequency_path, "cycles": cycles}
                
            job.status = "processed"
        except Exception as e:
            logging.error(f"Failed to process job {job.id}: {e}")
            job.status = "failed"
        finally:
            await self.channel.default_exchange.publish(
                aio_pika.Message(body=job.model_dump_json().encode()),
                routing_key=self.output_queue.name,
            )
