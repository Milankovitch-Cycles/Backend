from typing import Optional
from pandas import DataFrame
from src.modules.plots.plot.strategies.strategy import PlotStrategy
from src.modules.plots.plot.utils.utils import create_image

class PlotService:
    def __init__(self):
        pass
            
    def __init__(self, strategy: Optional[PlotStrategy] = None):
        self.strategy = strategy
        
    def set_strategy(self, strategy: PlotStrategy):
        self.strategy = strategy
    
    def plot(self, dataframe: DataFrame):
        self.strategy.plot(dataframe)
        
        return create_image()