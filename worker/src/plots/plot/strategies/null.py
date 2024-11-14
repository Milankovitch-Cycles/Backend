import missingno as mnso
from pandas import DataFrame
from src.plots.plot.strategies.strategy import PlotStrategy
from src.plots.plot.utils.utils import create_image

class Null(PlotStrategy):
    def __init__(self):
        super().__init__(path="null.png")
    
    def plot(self, dataframe: DataFrame, base_path: str):
        mnso.bar(dataframe)
        
        return {"title": "Missing Values", "image": create_image(f"{base_path}/{self.path}") }
        