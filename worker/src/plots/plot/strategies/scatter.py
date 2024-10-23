from pandas import DataFrame
from matplotlib import pyplot as plt
from src.plots.plot.mappers.mappers import map_code_to_description
from src.plots.plot.strategies.strategy import PlotStrategy

class Scatter(PlotStrategy):
    def __init__(self, column: str):
        self.column = column
        super().__init__(path=f"{map_code_to_description(self.column).replace(' ', '-')}/scatter.png")
    
    def plot(self, dataframe: DataFrame):
        plt.scatter(dataframe.index, dataframe[self.column], marker="o", alpha=0.4)
        
        x_label = map_code_to_description("DEPT")
        y_label = map_code_to_description(self.column)
        
        self.set_labels(x_label, y_label)
        