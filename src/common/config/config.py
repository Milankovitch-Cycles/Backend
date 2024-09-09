from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import os
from src.common.entities import Base
from src.common.entities.user_entity import UserEntity
from src.common.entities.code_entity import CodeEntity

SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"  # TO-DO: Add environment variable

try:
    engine = create_engine(url=SQLALCHEMY_DATABASE_URL)

except Exception as err:
    raise Exception("Unable to connect to DB, check your environment variables")

# Create session and model if necessary
session = scoped_session(sessionmaker(autoflush=False, bind=engine))
Base.query = session.query_property()

Base.metadata.create_all(bind=engine)
