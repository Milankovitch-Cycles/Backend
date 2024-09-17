from fastapi import HTTPException
from src.modules.auth.dependencies.dependencies import Permissions
from src.common.services.jwt.jwt_service import JwtService
from src.modules.codes.code_service import CodeService
from src.common.services.crypto.crypto_service import EncryptionService
from src.modules.users.user_service import UserService
from src.modules.auth.mappers.auth_mappers import (
    map_to_jwt_response,
    map_to_message_response,
)
from src.common.types.types import Token, Message


class RegisterService:
    def __init__(self):
        self.user_service = UserService()
        self.code_service = CodeService()
        self.encryption_service = EncryptionService()
        self.jwt_service = JwtService()

    def start(self, email: str, password: str) -> Token:
        user = self.user_service.get(email)

        if user:
            raise HTTPException(
                status_code=409,
                detail="We are sorry, an error occurred during the registration process",
            )

        hashed_password = self.encryption_service.encrypt(password)
        token = self.jwt_service.encode(
            {
                "email": email,
                "password": hashed_password,
                "permissions": Permissions.REGISTER.value,
            },
            expiration_time=1,
        )
        self.code_service.send(email)

        return map_to_jwt_response(token)

    def finish(self, email: str, password: str, code: str) -> Message:
        user = self.user_service.get(email)

        if user:
            raise HTTPException(
                status_code=409,
                detail="We are sorry, an error occurred during the registration process",
            )

        is_verified = self.code_service.validate(email, code)

        if not is_verified:
            raise HTTPException(
                status_code=409,
                detail="We are sorry, an error occurred during the registration process",
            )

        self.user_service.create(email, password)

        return map_to_message_response("User created successfully")
