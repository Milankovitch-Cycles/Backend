from sqlalchemy.orm import Session
from src.modules.auth.managers.login_service import LoginService
from src.modules.auth.managers.register_service import RegisterService
from src.common.types.types import Message, Token

class AuthService:
    def __init__(self, session: Session):
        self.register_service = RegisterService(session)
        self.login_service = LoginService(session)

    def register(self, email: str, password: str) -> Message:
        return self.register_service.register(email, password)

    def login(self, email: str, password: str) -> Token:
        return self.login_service.login(email, password)
