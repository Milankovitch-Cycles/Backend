from src.modules.auth.mappers.auth_mappers import map_to_user_dto
from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm
from src.modules.auth.dependencies.dependencies import (
    get_user_in_registration_flow,
    get_user_in_reset_password_flow,
    get_user_in_login_flow,
)
from src.common.entities.user_entity import UserEntity
from src.modules.auth.dtos.dtos import (
    FinishResetPasswordDto,
    InitResetPasswordDto,
    LoginRequestDto,
    StartRegistrationRequestDto,
    FinishRegistrationRequestDto,
    VerifyResetPasswordDto,
)
from .auth_service import AuthService
from src.common.types.types import Token, Message


class AuthController:
    def __init__(self):
        self.auth_service = AuthService()
        
    def me(
        self,
        user: UserEntity = Depends(get_user_in_login_flow),
    ) -> UserEntity:
        return map_to_user_dto(user)
        
    def start_registration(
        self,
        register_request_dto: StartRegistrationRequestDto,
    ) -> Token:
        email, password = (register_request_dto.email, register_request_dto.password)

        return self.auth_service.start_registration(email, password)

    def finish_registration(
        self,
        register_request_dto: FinishRegistrationRequestDto,
        user: UserEntity = Depends(get_user_in_registration_flow),
    ) -> Message:
        email, password, code = (user.email, user.password, register_request_dto.code)

        return self.auth_service.finish_registration(email, password, code)

    def login(
        self,
        login_request_dto: LoginRequestDto,
    ) -> Token:
        email, password = (login_request_dto.email, login_request_dto.password)

        return self.auth_service.login(email, password)

    def token(
        self,
        form_data: OAuth2PasswordRequestForm = Depends(),
    ) -> Token:
        email, password = (form_data.username, form_data.password)

        return self.auth_service.login(email, password)

    def start_password_reset(
        self,
        init_reset_password_dto: InitResetPasswordDto,
    ) -> Token:
        email = init_reset_password_dto.email

        return self.auth_service.start_password_reset(email)

    def verify_password_reset(
        self,
        verify_reset_password_dto: VerifyResetPasswordDto,
        user: UserEntity = Depends(get_user_in_reset_password_flow),
    ) -> Message:
        email, code = (user.email, verify_reset_password_dto.code)

        return self.auth_service.verify_password_reset(email, code)

    def finish_password_reset(
        self,
        finish_reset_password_dto: FinishResetPasswordDto,
        user: UserEntity = Depends(get_user_in_reset_password_flow),
    ) -> Message:
        email, password = (user.email, finish_reset_password_dto.password)

        return self.auth_service.finish_password_reset(email, password)
