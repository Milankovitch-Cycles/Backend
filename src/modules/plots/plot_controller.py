from typing import List, Optional
from fastapi import Depends, Query
from src.common.utils.split import parse_comma_separated_values
from src.common.entities.user_entity import UserEntity
from src.common.services.dataframe.dataframe_service import DataframeService
from src.modules.auth.dependencies.dependencies import get_user_in_login_flow
from src.modules.plots.plot_service import PlotService
from src.modules.wells.well_service import WellService

class PlotController:
    def __init__(self):
        self.plot_service = PlotService()
        self.well_service = WellService()
        self.dataframe_service = DataframeService()
        

    def plot_depth(
        self,
        well_id: int,
        user: UserEntity = Depends(get_user_in_login_flow),
        start: Optional[int] = None,
        end: Optional[int] = None,
        columns: Optional[List[str]] = Depends(parse_comma_separated_values),
    ):        
        dataframe = self.well_service.get_dataframe(well_id, user)
        filtered_dataframe = self.dataframe_service.filter_dataframe_by_index(dataframe, start, end)
        
        if not columns:
            columns = self.dataframe_service.get_columns(dataframe)
                
        return self.plot_service.plot_depth(filtered_dataframe, columns)

    def plot_histogram(
        self,
        well_id: int,
        column: str,
        user: UserEntity = Depends(get_user_in_login_flow),
        bins: Optional[int] = Query(30),
    ):
        dataframe = self.well_service.get_dataframe(well_id, user)
            
        return self.plot_service.plot_histogram(dataframe, column, bins)

            