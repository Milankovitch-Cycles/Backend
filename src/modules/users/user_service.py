from src.common.entities.user_entity import UserEntity
from sqlalchemy.orm import Session


class UserService:
    def __init__(self, session: Session):
        self.session = session

    def create(self, email: str, password: str) -> UserEntity:
        user = UserEntity(email=email, password=password)
        self.session.add(user)
        self.session.commit()
        return user

    def get_by_email(self, email: str) -> UserEntity:
        return self.session.query(UserEntity).filter(UserEntity.email == email).first()
