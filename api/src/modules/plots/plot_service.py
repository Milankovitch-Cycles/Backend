import matplotlib.pyplot as plt
from typing import List
from fastapi import HTTPException
from pandas import DataFrame
from src.common.utils.image import get_image
from src.modules.plots.strategies.plot_strategy_interface import PlotStrategyInterface

class PlotService:      
    def __init__(self, strategy: PlotStrategyInterface):
        self.strategy = strategy
        
    def set_strategy(self, strategy: PlotStrategyInterface):
        self.strategy = strategy
        
    def plot(self, dataframe: DataFrame, columns: List[str]):
        if not all(col in dataframe.columns for col in columns):
            raise HTTPException(status_code=400, detail=f"One or more columns {columns} not found in the DataFrame")
        
        self.strategy.plot(dataframe, columns)
        
        return get_image(plt)
    
        