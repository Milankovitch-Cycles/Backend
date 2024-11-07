from typing import Optional
from pydantic import BaseModel
from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, String, func, ForeignKey, JSON
from sqlalchemy.orm import relationship
from . import Base


class JobEntity(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True)
    well_id = Column(Integer, ForeignKey("wells.id"), nullable=False)
    well = relationship("WellEntity", back_populates="jobs")
    type = Column(String, nullable=False)
    parameters = Column(JSON, nullable=True)
    result = Column(JSON, nullable=True)
    status = Column(String, nullable=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    created_at = Column(DateTime, default=func.now(), nullable=False)


class GetJobModel(BaseModel):
    id: int
    user_id: int
    type: str
    parameters: dict | None
    result: dict | None
    status: str | None
    created_at: datetime
    graphs: list[str] | None = None

class CreateJobModel(BaseModel):
    type: str
    parameters: dict | None

class UpdateWellDto(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    