from typing import Optional, List
from fastapi import Query

def parse_comma_separated_values(columns: Optional[str] = Query(None)) -> List[str]:
    if columns is None:
        return []
    
    return [col.strip() for col in columns.split(",") if col.strip()]
