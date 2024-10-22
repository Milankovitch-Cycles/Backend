from pandas import DataFrame
from matplotlib import pyplot as plt
from worker.src.plots.plot.mappers.mappers import map_code_to_description
from worker.src.plots.plot.strategies.strategy import PlotStrategy


class Histogram(PlotStrategy):
    def __init__(self, column: str):
        self.column = column
        super().__init__(path=f"{map_code_to_description(column).replace(' ', '-')}/histogram.png")
    
    def plot(self, dataframe: DataFrame):
        plt.hist(dataframe[self.column], bins=30, color="blue", edgecolor="black", alpha=0.5)
        
        x_label = map_code_to_description(self.column)
        y_label = map_code_to_description("FREQ")

        self.set_labels(x_label, y_label)
        
