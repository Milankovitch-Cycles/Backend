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
