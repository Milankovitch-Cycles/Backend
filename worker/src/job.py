from pydantic import BaseModel
from datetime import datetime


class Job(BaseModel):
    id: int
    well_id: int
    type: str
    parameters: dict | None
    result: dict | None
    status: str | None
    user_id: int
    created_at: datetime

class ProcessResult(BaseModel):
    job: Job
    metadata: dict | None