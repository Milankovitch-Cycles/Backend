from src.processor.graphs_processor import GraphsProcessor
from src.processor.milankovic_cycles_processor import MilankovicCyclesProcessor
from src.processor.new_well_processor import NewWellProcessor
from src.processor.prediction_processor import PredictionProcessor


class JobProcessorManager:
    def get_strategies(self, type: str):
        if(type == "NEW_WELL"):
            return [NewWellProcessor()]
        elif(type == "GRAPHS"):
            return [GraphsProcessor()]
        elif(type == "MILANKOVIC_CYCLES"):
            return [MilankovicCyclesProcessor()]
        elif(type == "PREDICTION"):
            return [PredictionProcessor()]
        else:
            return []

    def process_job(self, job, dataframe):
        processors = self.get_strategies(job.type)
        
        result = {}
        for processor in processors:
            result.update(processor.process(job, dataframe))
        
        return result
