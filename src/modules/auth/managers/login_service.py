from fastapi import HTTPException
from src.common.entities.user_entity import UserEntity
from src.common.services.crypto.crypto_service import EncryptionService
from src.common.services.jwt.jwt_service import JwtService
from src.modules.users.user_service import UserService
from src.common.types.types import Token
from src.modules.auth.mappers.auth_mappers import (
    map_to_jwt_response,
)


class LoginService:
    def __init__(self):
        self.user_service = UserService()
        self.encryption_service = EncryptionService()
        self.jwt_service = JwtService()

    def login(self, email: str, password: str) -> Token:
        user = self.user_service.get(email)

        if user is None:
            raise HTTPException(
                status_code=500,
                detail="We are sorry, an error occurred during the login process",
            )

        decrypted_password = self.encryption_service.decrypt(user.password)

        if decrypted_password != password:
            raise HTTPException(
                status_code=500,
                detail="We are sorry, an error occurred during the login process",
            )

        token = self.jwt_service.encode(email)

        return map_to_jwt_response(token)

    def get_user(self, jwt: str) -> UserEntity:
        message = self.jwt_service.decode(jwt)

        user = self.user_service.get(message["sub"])

        if user is None:
            raise HTTPException(
                status_code=401,
                detail="Invalid credentials",
            )

        return user
