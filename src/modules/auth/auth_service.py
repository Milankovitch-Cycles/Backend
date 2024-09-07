from sqlalchemy.orm import Session
from src.modules.auth.managers.reset_password_service import ResetPasswordService
from src.modules.auth.managers.login_service import LoginService
from src.modules.auth.managers.register_service import RegisterService
from src.common.types.types import Message, Token

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
