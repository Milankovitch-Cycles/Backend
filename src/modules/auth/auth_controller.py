from fastapi import Depends
from src.modules.auth.dependencies.dependencies import (
    get_user_in_reset_password_flow,
)
from src.common.entities.user_entity import UserEntity
from src.modules.auth.dtos.dtos import (
    FinishResetPasswordDto,
    InitResetPasswordDto,
    LoginRequestDto,
    RegisterRequestDto,
    VerifyResetPasswordDto,
)
from .auth_service import AuthService


class AuthController:
    def __init__(self):
        self.auth_service = AuthService()

    def register(
        self,
        register_request_dto: RegisterRequestDto,
    ):
        email, password = (register_request_dto.email, register_request_dto.password)

        return self.auth_service.register(email, password)

    def login(
        self,
        login_request_dto: LoginRequestDto,
    ):
        email, password = (login_request_dto.email, login_request_dto.password)

        return self.auth_service.login(email, password)

    def init_reset_password(
        self,
        init_reset_password_dto: InitResetPasswordDto,
    ):
        email = init_reset_password_dto.email

        return self.auth_service.init_reset_password(email)

    def verify_reset_password(
        self,
        verify_reset_password_dto: VerifyResetPasswordDto,
        user: UserEntity = Depends(get_user_in_reset_password_flow),
    ):
        email, code = (user.email, verify_reset_password_dto.code)

        return self.auth_service.verify_reset_password(email, code)

    def finish_reset_password(
        self,
        finish_reset_password_dto: FinishResetPasswordDto,
        user: UserEntity = Depends(get_user_in_reset_password_flow),
    ):
        email, password = (user.email, finish_reset_password_dto.password)

        return self.auth_service.finish_reset_password(email, password)
