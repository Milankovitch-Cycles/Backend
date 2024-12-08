from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from . import Base

class JobTypeEntity(Base):
    __tablename__ = "job_types"

    id = Column(Integer, primary_key=True)
    code = Column(String, nullable=False)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)


class GetJobTypeModel(BaseModel):
    id: int
    code: str
    name: str
    description: str

    