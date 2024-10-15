from typing import List
from pandas import DataFrame
from src.modules.plots.strategies.plot_strategy_interface import PlotStrategyInterface

class DepthPlotStrategy(PlotStrategyInterface):      
    def __init__(self):
        pass
      
    def plot(self, dataframe: DataFrame, columns: List[str]):
        return dataframe.plot(y=columns)
        