import seaborn as sns
from pandas import DataFrame
from matplotlib import pyplot as plt
from src.plots.plot.mappers.mappers import map_code_to_description
from src.plots.plot.strategies.strategy import PlotStrategy


class Histogram(PlotStrategy):
    def __init__(self, column: str):
        self.column = column
        super().__init__(path=f"{map_code_to_description(column).replace(' ', '-')}/histogram.png")
    
    def plot(self, dataframe: DataFrame):
        sns.set_theme(style="whitegrid")

        plt.figure(figsize=(10, 6))
        sns.histplot(dataframe[self.column], bins=30, kde=True, color="dodgerblue", edgecolor="black", alpha=0.7)

        x_label = map_code_to_description(self.column)
        y_label = map_code_to_description("FREQ")

        plt.title(f"{x_label} Histogram", fontsize=16)    
        
        self.set_labels(x_label, y_label)
        
