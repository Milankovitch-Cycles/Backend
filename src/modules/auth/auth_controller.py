from fastapi import Depends
from requests import Session
from src.modules.auth.dependencies.dependencies import (
    get_user_in_reset_password_flow,
    get_auth_service,
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

# TO-DO: Me gustaria inicializar el servicio en el controlador pero me rompe el Depends del get_auth_service


class AuthController:
    def register(
        self,
        register_request_dto: RegisterRequestDto,
        auth_service: AuthService = Depends(get_auth_service),
    ):
        email, password = (register_request_dto.email, register_request_dto.password)

        return auth_service.register(email, password)

    def login(
        self,
        login_request_dto: LoginRequestDto,
        auth_service: AuthService = Depends(get_auth_service),
    ):
        email, password = (login_request_dto.email, login_request_dto.password)

        return auth_service.login(email, password)

    def init_reset_password(
        self,
        init_reset_password_dto: InitResetPasswordDto,
        auth_service: AuthService = Depends(get_auth_service),
    ):
        email = init_reset_password_dto.email

        return auth_service.init_reset_password(email)

    def verify_reset_password(
        self,
        verify_reset_password_dto: VerifyResetPasswordDto,
        user: UserEntity = Depends(get_user_in_reset_password_flow),
        auth_service: AuthService = Depends(get_auth_service),
    ):
        email, code = (user.email, verify_reset_password_dto.code)

        return auth_service.verify_reset_password(email, code)

    def finish_reset_password(
        self,
        finish_reset_password_dto: FinishResetPasswordDto,
        user: UserEntity = Depends(get_user_in_reset_password_flow),
        auth_service: AuthService = Depends(get_auth_service),
    ):
        email, password = (user.email, finish_reset_password_dto.password)

        return auth_service.finish_reset_password(email, password)
