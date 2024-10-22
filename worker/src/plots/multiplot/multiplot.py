from typing import List
from pandas import DataFrame
from worker.src.plots.plot.plot import PlotService
from worker.src.plots.plot.strategies.strategy import PlotStrategy

class MultiplotService():
    def __init__(self, strategies: List[PlotStrategy]):
        self.strategies = strategies
        self.plot_service = PlotService()
        
    def add_plot(self, plot: PlotStrategy):
        self.strategies.append(plot)

    def plot(self, dataframe: DataFrame, path: str):
        images = []
        
        for strategy in self.strategies:
            self.plot_service.set_strategy(strategy)
            image_path = self.plot_service.plot(dataframe, path)
            images.append(image_path)

        return images            
    
# TO-DO: Remove this comment

# Example to use

# multiplot = Factory.make_multiplot()
# dataframe = lasio.read("data/data.LAS").df()
# graphs = multiplot.plot(dataframe, "./graphics-test")
        