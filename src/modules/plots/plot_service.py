import matplotlib.pyplot as plt
from typing import List
from fastapi import HTTPException
from pandas import DataFrame
from src.common.utils.image import get_image

class PlotService:      
    def __init__(self):
        pass
      
    def plot_depth(self, dataframe: DataFrame, columns: List[str]):
        if not all(col in dataframe.columns for col in columns):
            raise HTTPException(status_code=400, detail=f"One or more columns {columns} not found in the DataFrame")
        
        dataframe.plot(y=columns)
        
        return get_image(plt)
    
    def plot_histogram(self, dataframe: DataFrame, column: str, bins: int):
        if column not in dataframe.columns:
            raise HTTPException(status_code=400, detail=f"Column {column} not found in the DataFrame")
        
        plt.hist(dataframe[column], bins, edgecolor="black")
        
        return get_image(plt)
    
        