import seaborn as sns
import matplotlib.pyplot as plt
from pandas import DataFrame
from src.plots.plot.mappers.mappers import map_code_to_description
from src.plots.plot.strategies.strategy import PlotStrategy

class Scatter(PlotStrategy):
    def __init__(self, column: str):
        self.column = column
        super().__init__(path=f"{map_code_to_description(self.column).replace(' ', '-')}/scatter.png")
    
    def plot(self, dataframe: DataFrame):
        plt.figure(figsize=(10, 6))
        
        sns.scatterplot(x=dataframe.index, y=dataframe[self.column], 
                        marker="o", alpha=0.5, s=80, color="dodgerblue", 
                        edgecolor=None, linewidth=0.5)
                
        x_label = map_code_to_description("DEPT")
        y_label = map_code_to_description(self.column)
        
        plt.title(f"Scatter Plot of {y_label}", fontsize=16)
        
        self.set_labels(x_label, y_label)
        