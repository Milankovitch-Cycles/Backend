from abc import ABC, abstractmethod

class JobProcessor(ABC):
    @abstractmethod
    def process(self, job, dataframe):
        pass
