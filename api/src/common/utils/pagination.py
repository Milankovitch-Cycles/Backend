from typing import List
from pydantic import BaseModel

class Pagination(BaseModel):
    limit: int
    offset: int
    total: int
    previous_offset: int
    next_offset: int
    total_pages: int
    
def get_pagination(limit: int, offset: int, count: int) -> Pagination:
    return Pagination(
        limit=limit,
        offset=offset,
        total=count,
        previous_offset=offset - limit if offset - limit >= 0 else 0,
        next_offset=offset + limit if offset + limit < count else 0,
        total_pages=count // limit)
    