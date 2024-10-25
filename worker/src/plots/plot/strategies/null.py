import missingno as mnso
from pandas import DataFrame
from src.plots.plot.strategies.strategy import PlotStrategy

class Null(PlotStrategy):
    def __init__(self):
        super().__init__(path="null.png")
    
    def plot(self, dataframe: DataFrame):
        mnso.bar(dataframe)
        