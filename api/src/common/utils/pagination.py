from typing import List
from pydantic import BaseModel

class Pagination(BaseModel):
    limit: int
    offset: int
    total: int
    previous_offset: int
    next_offset: int
    total_pages: int
    
def get_pagination(limit: int, offset: int, data: List[object]) -> Pagination:
    return Pagination(
        limit=limit,
        offset=offset,
        total=len(data),
        previous_offset=offset - limit if offset - limit >= 0 else 0,
        next_offset=offset + limit if offset + limit < len(data) else 0,
        total_pages=len(data) // limit)
    