from typing import List, Optional
from fastapi import HTTPException
from pandas import DataFrame

class DataframeService:
    def get_columns(self, dataframe: DataFrame) -> List[str]:
        return dataframe.columns.tolist()
    
    def filter_dataframe_by_index(self, dataframe: DataFrame, start: Optional[int], end: Optional[int]) -> DataFrame:
        if start is not None and end is not None and start > end:
            raise HTTPException(status_code=400, detail=f"Start index must be less than end index")
        
        min_index = dataframe.index.min()
        max_index = dataframe.index.max()
            
        if start is None or start < min_index:
            start = min_index
                
        if end is None or end > max_index:
            end = max_index
                
        return dataframe[(dataframe.index >= start) & (dataframe.index <= end)]