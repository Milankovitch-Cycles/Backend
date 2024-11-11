from fastapi import HTTPException
from src.modules.auth.dependencies.dependencies import Permissions
from src.common.services.hash.hash_service import HashService
from src.common.services.jwt.jwt_service import JwtService
from src.modules.users.user_service import UserService
from src.common.types.types import Token
from src.modules.auth.mappers.auth_mappers import (
    map_to_jwt_response,
)


class LoginService:
    def __init__(self):
        self.user_service = UserService()
        self.hash_service = HashService()
        self.jwt_service = JwtService()

    def login(self, email: str, password: str) -> Token:
        user = self.user_service.get_by_email(email)

        if user is None:
            raise HTTPException(
                status_code=500,
                detail="We are sorry, an error occurred during the login process",
            )

        hashed_password = self.hash_service.hash(password)

        if user.password != hashed_password:
            raise HTTPException(
                status_code=500,
                detail="We are sorry, an error occurred during the login process",
            )

        token = self.jwt_service.encode(
            {"sub": email, "permissions": Permissions.LOGIN.value}
        )

        return map_to_jwt_response(token)
