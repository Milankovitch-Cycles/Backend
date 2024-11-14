from typing import Optional
from pandas import DataFrame
from src.plots.plot.strategies.strategy import PlotStrategy


class PlotService:
    def __init__(self):
        pass
            
    def __init__(self, strategy: Optional[PlotStrategy] = None):
        self.strategy = strategy
        
    def set_strategy(self, strategy: PlotStrategy):
        self.strategy = strategy
    
    def plot(self, dataframe: DataFrame, base_path: str):
        return self.strategy.plot(dataframe, base_path)
        
