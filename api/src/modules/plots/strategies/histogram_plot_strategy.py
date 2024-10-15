from typing import List, Optional
from pandas import DataFrame
from src.modules.plots.strategies.plot_strategy_interface import PlotStrategyInterface

class HistogramPlotStrategy(PlotStrategyInterface):      
    def __init__(self, bins: Optional[int] = 30, color: Optional[str] = "black"):
        self.bins = bins
        self.color = color
    
    def plot(self, dataframe: DataFrame, columns: List[str]):
        return dataframe.hist(column=columns, bins=self.bins, edgecolor=self.color)
                        