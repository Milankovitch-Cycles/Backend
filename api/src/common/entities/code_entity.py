from sqlalchemy import Column, DateTime, ForeignKey, Integer, Boolean, String, func
from . import Base


class CodeEntity(Base):
    __tablename__ = "codes"

    id = Column(Integer, primary_key=True)
    email = Column(Integer, ForeignKey("users.email"), nullable=False)
    code = Column(String, nullable=False)
    verified = Column(Boolean, default=False, nullable=False)
    created_at = Column(DateTime, default=func.now(), nullable=False)
