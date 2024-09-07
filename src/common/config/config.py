from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.common.entities import Base
from src.common.entities.user_entity import UserEntity
from src.common.entities.code_entity import CodeEntity

SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"  # TO-DO: Add environment variable
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


Base.metadata.create_all(bind=engine)
