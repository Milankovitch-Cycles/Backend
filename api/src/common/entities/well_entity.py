from pydantic import BaseModel
from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, String, func, ForeignKey
from . import Base


class WellEntity(Base):
    __tablename__ = "wells"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=True)
    description = Column(String, nullable=True)
    filename = Column(String, nullable=True)
    well_metadata = Column(String, nullable=True)
    status = Column(String, nullable=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    created_at = Column(DateTime, default=func.now(), nullable=False)


class CreateWellModel(BaseModel):
    name: str | None = None
    description: str | None = None
    filename: str | None = None


class GetWellModel(BaseModel):
    id: int | None
    name: str | None
    description: str | None
    filename: str | None
    well_metadata: str | None
    status: str | None
    user_id: int | None
    created_at: datetime | None
