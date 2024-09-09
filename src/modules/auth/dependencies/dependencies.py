from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from src.modules.auth.auth_service import AuthService


def get_user(
    auth_service: AuthService = Depends(),
    token: str = Depends(OAuth2PasswordBearer(tokenUrl="/auth/login")),
):
    return auth_service.get_user_in_session(token)


def get_user_in_reset_password_flow(
    auth_service: AuthService = Depends(),
    token: str = Depends(OAuth2PasswordBearer(tokenUrl="/auth/reset_password/init")),
):
    return auth_service.get_user_in_reset_password_flow(token)
