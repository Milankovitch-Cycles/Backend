from src.plots.multiplot.multiplot import MultiplotService
from src.plots.plot.strategies.depth import Depth
from src.plots.plot.strategies.histogram import Histogram
from src.plots.plot.strategies.null import Null
from src.plots.plot.strategies.scatter import Scatter
from src.plots.plot.strategies.heatmap import Heatmap
from src.plots.plot.strategies.multiple_curve import MultipleCurve
from src.plots.plot.strategies.pair import Pair


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
            Null(),
            Heatmap(),
            MultipleCurve(),
            Pair()
        ]
        
        return MultiplotService(strategies)
