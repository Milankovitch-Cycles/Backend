from abc import ABC, abstractmethod
import os
from pandas import DataFrame
from matplotlib import pyplot as plt

class PlotStrategy(ABC):
    
    def __init__(self, path: str):
        self.path = path

    @abstractmethod
    def plot(self, dataframe: DataFrame):
        pass
    
    def set_labels(self, x_label: str, y_label: str):
        plt.xlabel(x_label, fontdict={'fontsize': 14})
        plt.ylabel(y_label, fontdict={'fontsize': 14})
    
