import seaborn as sns
import matplotlib.pyplot as plt
from pandas import DataFrame
from src.plots.plot.mappers.mappers import map_code_to_description
from src.plots.plot.strategies.strategy import PlotStrategy
from src.plots.plot.utils.utils import create_image

class Scatter(PlotStrategy):
    def __init__(self, column: str):
        self.column = column
        super().__init__(path=f"{map_code_to_description(self.column).replace(' ', '-')}/scatter.png")
    
    def plot(self, dataframe: DataFrame, base_path: str):
        plt.figure(figsize=(10, 6))
        
        sns.scatterplot(x=dataframe.index, y=dataframe[self.column], 
                        marker="o", alpha=0.5, s=80, color="dodgerblue", 
                        edgecolor=None, linewidth=0.5)
                
        x_label = map_code_to_description("DEPT")
        y_label = map_code_to_description(self.column)
        
        title = f"Scatter Plot of {y_label}"
        plt.title(title, fontsize=16)
        
        self.set_labels(x_label, y_label)
        
        return {"title": f"Scatter Plot of {y_label}", "image": create_image(f"{base_path}/{self.path}") }
        