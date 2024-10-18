from pandas import DataFrame
from matplotlib import pyplot as plt
from src.modules.plots.plot.strategies.strategy import PlotStrategy
from src.modules.plots.data import descriptions

class Scatter(PlotStrategy):
    def __init__(self, column: str):
        self.column = column
    
    def plot(self, dataframe: DataFrame):
        plt.scatter(dataframe.index, dataframe[self.column], marker="o", alpha=0.4)
        self.set_labels(descriptions["DEPT"], descriptions[self.column])