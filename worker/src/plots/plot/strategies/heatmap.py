from pandas import DataFrame
from matplotlib import pyplot as plt
import seaborn as sns
from src.plots.plot.strategies.strategy import PlotStrategy

class Heatmap(PlotStrategy):
    def __init__(self):
        super().__init__(path="heatmap.png")

    def plot(self, dataframe: DataFrame):
        plt.figure(figsize=(10, 8))
        sns.heatmap(dataframe.corr(), annot=True, cmap="coolwarm", center=0, linewidths=0.5)
        
        plt.title("Heatmap of Variable Correlations", fontsize=16)

