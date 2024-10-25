from pandas import DataFrame
from matplotlib import pyplot as plt
from src.plots.plot.mappers.mappers import map_code_to_description
from src.plots.plot.strategies.strategy import PlotStrategy

class MultipleCurve(PlotStrategy):
    def __init__(self):
        super().__init__(path="multiple_curve_plot.png")

    def plot(self, dataframe: DataFrame):
        plt.figure(figsize=(10, 8))
        
        for column in dataframe.columns:
            plt.plot(dataframe[column], dataframe.index, label=map_code_to_description(column), linewidth=1.5)
        
        plt.gca().invert_yaxis()
        plt.title("Multiple Curve Plot", fontsize=16)
        plt.legend()
        
        x_label = "Value"
        y_label = map_code_to_description("DEPT")
        
        self.set_labels(x_label, y_label)