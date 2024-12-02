from src.processor.job_processor import JobProcessor
from src.plots.factory.factory import Factory

class GraphsProcessor(JobProcessor):
    def __init__(self):
        self.multiplot = Factory.make_multiplot()
        
    def process(self, job, dataframe):
        images = self.multiplot.plot(dataframe, f"./static/{job.well_id}/{job.id}/graphs")
        return {"graphs": images}