from src.common.entities.user_entity import UserEntity
from src.common.config.config import session


class UserService:
    def get_by_id(self, id: int) -> UserEntity:
        return session.query(UserEntity).filter(UserEntity.id == id).first()
    
    def get_by_email(self, email: str) -> UserEntity:
        return session.query(UserEntity).filter(UserEntity.email == email).first()

    def create(self, user: UserEntity) -> UserEntity:
        session.add(user)
        session.commit()
        return user

    def update(self, email: str, new_attributes: dict) -> UserEntity:
        user = self.get_by_email(email)
        for attr, value in new_attributes.items():
            setattr(user, attr, value)
        session.add(user)
        session.commit()
        return user
