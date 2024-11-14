from pandas import DataFrame
from matplotlib import pyplot as plt
from src.plots.plot.mappers.mappers import map_code_to_description
from src.plots.plot.strategies.strategy import PlotStrategy
from src.plots.plot.utils.utils import create_image


class Depth(PlotStrategy):
    def __init__(self, column: str):
        self.column = column
        super().__init__(path=f"{map_code_to_description(self.column).replace(' ', '-')}/depth.png")
    
    def plot(self, dataframe: DataFrame, base_path: str):
        plt.figure(figsize=(10, 6))

        plt.plot(dataframe[self.column], dataframe.index, color = "dodgerblue")
        plt.gca().invert_yaxis()
       
        x_label = map_code_to_description(self.column)
        y_label = map_code_to_description("DEPT")
        
        title = f"Depth versus {x_label} chart"
        
        plt.title(title, fontsize=16)    
        
        self.set_labels(x_label, y_label)     
           
        return {"title": title, "image": create_image(f"{base_path}/{self.path}") }