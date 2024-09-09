from src.common.entities.user_entity import UserEntity
from sqlalchemy.orm import Session


class UserService:
    def __init__(self, session: Session):
        self.session = session

    def create_user(self, email: str, password: str) -> UserEntity:
        user = UserEntity(email=email, password=password)
        self.session.add(user)
        self.session.commit()
        return user

    def get_by_email(self, email: str) -> UserEntity:
        return self.session.query(UserEntity).filter(UserEntity.email == email).first()

    def update_user(self, email: str, new_attributes: dict) -> UserEntity:
        user = self.get_by_email(email)
        for attr, value in new_attributes.items():
            setattr(user, attr, value)
        self.session.add(user)
        self.session.commit()
        return user
