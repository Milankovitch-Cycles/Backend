
from abc import ABC, abstractmethod
from typing import List
from pandas import DataFrame

class PlotStrategyInterface(ABC):

    @abstractmethod
    def plot(self, dataframe: DataFrame, columns: List[str]):
        pass