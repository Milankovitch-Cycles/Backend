import seaborn as sns
from pandas import DataFrame
from matplotlib import pyplot as plt
from src.plots.plot.strategies.strategy import PlotStrategy
from src.plots.plot.utils.utils import create_image


class Pair(PlotStrategy):
    def __init__(self):
        super().__init__(path="pairplot.png")

    def plot(self, dataframe: DataFrame, base_path: str):
        sns.pairplot(dataframe, corner=True, plot_kws={'alpha':0.5})
        title = "Pairplot of Variables"
        plt.suptitle(title, fontsize=16)
        
        return {"title": "Pairplot of Variables", "image": create_image(f"{base_path}/{self.path}") }