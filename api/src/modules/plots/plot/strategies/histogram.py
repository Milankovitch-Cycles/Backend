from pandas import DataFrame
from matplotlib import pyplot as plt
from src.modules.plots.plot.strategies.strategy import PlotStrategy
from src.modules.plots.data import descriptions

class Histogram(PlotStrategy):
    def __init__(self, column: str):
        self.column = column
    
    def plot(self, dataframe: DataFrame):
        plt.hist(dataframe[self.column], bins=30, color="blue", edgecolor="black", alpha=0.5)
        self.set_labels(descriptions[self.column], descriptions["FREQ"])    
  