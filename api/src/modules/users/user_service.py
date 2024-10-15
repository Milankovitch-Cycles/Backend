from src.common.entities.user_entity import UserEntity
from src.common.config.config import session


class UserService:
    def get(self, email: str) -> UserEntity:
        return session.query(UserEntity).filter(UserEntity.email == email).first()

    def create(self, email: str, password: str) -> UserEntity:
        user = UserEntity(email=email, password=password)
        session.add(user)
        session.commit()
        return user

    def update(self, email: str, new_attributes: dict) -> UserEntity:
        user = self.get(email)
        for attr, value in new_attributes.items():
            setattr(user, attr, value)
        session.add(user)
        session.commit()
        return user
