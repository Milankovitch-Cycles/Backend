from src.modules.plots.multiplot.multiplot import MultiplotService
from src.modules.plots.plot.strategies.depth import Depth
from src.modules.plots.plot.strategies.histogram import Histogram
from src.modules.plots.plot.strategies.null import Null
from src.modules.plots.plot.strategies.scatter import Scatter

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
            Null()]
        return MultiplotService(strategies)
