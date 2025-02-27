from sqlalchemy import Column, DateTime, Integer, String, Boolean, func
from . import Base


class UserEntity(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    first_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)
    pic = Column(String, nullable=True)
    created_at = Column(DateTime, default=func.now(), nullable=False)
