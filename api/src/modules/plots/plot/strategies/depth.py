from pandas import DataFrame
from matplotlib import pyplot as plt
from src.modules.plots.plot.strategies.strategy import PlotStrategy
from src.modules.plots.data import descriptions

class Depth(PlotStrategy):
    def __init__(self, column: str):
        super().__init__(path=f"{descriptions[column].replace(' ', '-')}/depth.png")
        self.column = column
    
    def plot(self, dataframe: DataFrame):
        plt.plot(dataframe[self.column], dataframe.index, color = "blue")
        plt.gca().invert_yaxis()
        self.set_labels(descriptions[self.column], descriptions["DEPT"])        
