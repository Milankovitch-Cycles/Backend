from src.plots.multiplot.multiplot import MultiplotService
from src.plots.plot.strategies.depth import Depth
from src.plots.plot.strategies.histogram import Histogram
from src.plots.plot.strategies.null import Null
from src.plots.plot.strategies.scatter import Scatter


class Factory:
    
    @staticmethod
    def make_multiplot():
        strategies = [
            Depth("GR"), 
            Histogram("GR"), 
            Scatter("GR"),
            Depth("DEN"),
            Histogram("DEN"),
            Scatter("DEN"),
            Depth("NEU"),
            Histogram("NEU"),
            Scatter("NEU"), 
            Null()
        ]
        
        return MultiplotService(strategies)
