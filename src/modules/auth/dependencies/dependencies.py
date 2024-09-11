from enum import Enum
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from src.common.entities.user_entity import UserEntity
from src.common.services.jwt.jwt_service import JwtService
from src.modules.users.user_service import UserService

# Esto se podria hacer mucho mejor con decoradores, pero la verdad es que no se como hacerlo. Lo que intente no me
# funciono. Habria que investigarlo. Por ahora, lo dejo asi.

jwt_service = JwtService()
user_service = UserService()


class Permissions(Enum):
    LOGIN = "login"
    RESET_PASSWORD = "reset_password"
    REGISTER = "register"


def validate_permissions(message, permissions):
    if message["permissions"] != permissions:
        raise HTTPException(
            status_code=401,
            detail="Unauthorized",
        )

    return permissions


def validate_user(message):
    user = user_service.get(message["sub"])
    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found",
        )

    return user


def get_user(
    token: str,
    permissions: str,
):
    message = jwt_service.decode(token)
    validate_permissions(message, permissions)
    return validate_user(message)


def get_user_in_login_flow(
    token: str = Depends(OAuth2PasswordBearer(tokenUrl="/auth/login")),
):
    message = jwt_service.decode(token)
    validate_permissions(message, Permissions.LOGIN.value)
    return validate_user(message)


def get_user_in_reset_password_flow(
    token: str = Depends(OAuth2PasswordBearer(tokenUrl="/auth/password/reset/start")),
):
    message = jwt_service.decode(token)
    validate_permissions(message, Permissions.RESET_PASSWORD.value)
    return validate_user(message)


def get_user_in_registration_flow(
    token: str = Depends(OAuth2PasswordBearer(tokenUrl="/auth/register/start")),
):
    message = jwt_service.decode(token)
    validate_permissions(message, Permissions.REGISTER.value)
    user = UserEntity(email=message["email"], password=message["password"])
    return user
