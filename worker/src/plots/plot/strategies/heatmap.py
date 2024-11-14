from pandas import DataFrame
from matplotlib import pyplot as plt
import seaborn as sns
from src.plots.plot.strategies.strategy import PlotStrategy
from src.plots.plot.utils.utils import create_image

class Heatmap(PlotStrategy):
    def __init__(self):
        super().__init__(path="heatmap.png")

    def plot(self, dataframe: DataFrame, base_path: str):
        plt.figure(figsize=(10, 8))
        sns.heatmap(dataframe.corr(), annot=True, cmap="coolwarm", center=0, linewidths=0.5)
        
        title = "Heatmap of Variable Correlations"
        plt.title(title, fontsize=16)
        
        return {"title": title, "image": create_image(f"{base_path}/{self.path}") }

