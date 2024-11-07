from pandas import DataFrame
from matplotlib import pyplot as plt
from src.plots.plot.mappers.mappers import map_code_to_description
from src.plots.plot.strategies.strategy import PlotStrategy


class Depth(PlotStrategy):
    def __init__(self, column: str):
        self.column = column
        super().__init__(path=f"{map_code_to_description(self.column).replace(' ', '-')}/depth.png")
    
    def plot(self, dataframe: DataFrame):
        plt.figure(figsize=(10, 6))

        plt.plot(dataframe[self.column], dataframe.index, color = "dodgerblue")
        plt.gca().invert_yaxis()
       
        x_label = map_code_to_description(self.column)
        y_label = map_code_to_description("DEPT")
        
        plt.title(f"Depth versus {x_label} chart", fontsize=16)    
        
        self.set_labels(x_label, y_label)        
