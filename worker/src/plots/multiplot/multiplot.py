from typing import List
from pandas import DataFrame
from src.plots.plot.plot import PlotService
from src.plots.plot.strategies.strategy import PlotStrategy

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
            image = self.plot_service.plot(dataframe, path)
            images.append(image)

        return images            
