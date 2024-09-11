from src.modules.auth.managers.reset_password_service import ResetPasswordService
from src.modules.auth.managers.login_service import LoginService
from src.modules.auth.managers.register_service import RegisterService
from src.common.types.types import Message, Token


class AuthService:
    def __init__(self):
        self.register_service = RegisterService()
        self.login_service = LoginService()
        self.reset_pasword_service = ResetPasswordService()

    def start_registration(self, email: str, password: str) -> Token:
        return self.register_service.start(email, password)

    def finish_registration(self, email: str, password: str, code: str) -> Message:
        return self.register_service.finish(email, password, code)

    def login(self, email: str, password: str) -> Token:
        return self.login_service.login(email, password)

    def start_password_reset(self, email: str) -> Token:
        return self.reset_pasword_service.start(email)

    def verify_password_reset(self, email: str, code: str) -> Message:
        return self.reset_pasword_service.verify(email, code)

    def finish_password_reset(self, email: str, new_password: str) -> Message:
        return self.reset_pasword_service.finish(email, new_password)
