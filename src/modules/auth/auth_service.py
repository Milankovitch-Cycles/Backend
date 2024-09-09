from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from src.common.entities.user_entity import UserEntity
from src.modules.auth.managers.reset_password_service import ResetPasswordService
from src.modules.auth.managers.login_service import LoginService
from src.modules.auth.managers.register_service import RegisterService
from src.common.types.types import Message, Token

oauth2 = OAuth2PasswordBearer(tokenUrl="/auth/login")


class AuthService:
    def __init__(self, session: Session):
        self.register_service = RegisterService(session)
        self.login_service = LoginService(session)
        self.reset_pasword_service = ResetPasswordService(session)

    def register(self, email: str, password: str) -> Message:
        return self.register_service.register(email, password)

    def login(self, email: str, password: str) -> Token:
        return self.login_service.login(email, password)

    def init_reset_password(self, email: str) -> Token:
        return self.reset_pasword_service.init(email)

    def verify_reset_password(self, email: str, code: str):
        return self.reset_pasword_service.verify(email, code)

    def finish_reset_password(self, email: str, new_password: str):
        return self.reset_pasword_service.finish(email, new_password)

    def get_user_in_session(self, jwt: str = Depends(oauth2)) -> UserEntity:
        return self.login_service.get_user(jwt)

    def get_user_in_reset_password_flow(self, jwt: str = Depends(oauth2)) -> UserEntity:
        return self.reset_pasword_service.get_user(jwt)
