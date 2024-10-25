import seaborn as sns
from pandas import DataFrame
from matplotlib import pyplot as plt
from src.plots.plot.strategies.strategy import PlotStrategy


class Pair(PlotStrategy):
    def __init__(self):
        super().__init__(path="pairplot.png")

    def plot(self, dataframe: DataFrame):
        sns.pairplot(dataframe, corner=True, plot_kws={'alpha':0.5})
        plt.suptitle("Pairplot of Variables", fontsize=16)