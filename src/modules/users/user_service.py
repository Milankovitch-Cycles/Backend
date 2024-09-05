from src.common.entities.user_entity import User
from sqlalchemy.orm import Session


class UserService:
    def __init__(self, session: Session):
        self.session = session

    def create(self, email: str, password: str) -> User:
        user = User(email=email, password=password)
        self.session.add(user)
        self.session.commit()
        return user

    def get_by_email(self, email: str) -> User:
        return self.session.query(User).filter(User.email == email).first()
