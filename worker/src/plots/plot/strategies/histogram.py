import seaborn as sns
from pandas import DataFrame
from matplotlib import pyplot as plt
from src.plots.plot.mappers.mappers import map_code_to_description
from src.plots.plot.strategies.strategy import PlotStrategy
from src.plots.plot.utils.utils import create_image


class Histogram(PlotStrategy):
    def __init__(self, column: str):
        self.column = column
        super().__init__(path=f"{map_code_to_description(column).replace(' ', '-')}/histogram.png")
    
    def plot(self, dataframe: DataFrame, base_path: str):
        sns.set_theme(style="whitegrid")

        plt.figure(figsize=(10, 6))
        sns.histplot(dataframe[self.column], bins=30, kde=True, color="dodgerblue", edgecolor="black", alpha=0.7)

        x_label = map_code_to_description(self.column)
        y_label = map_code_to_description("FREQ")

        title = f"{x_label} Histogram"
        plt.title(title, fontsize=16)    
        
        self.set_labels(x_label, y_label)
        
        return {"title": title, "image": create_image(f"{base_path}/{self.path}") }

        
