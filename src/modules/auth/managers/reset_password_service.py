from fastapi import HTTPException
from src.modules.auth.dependencies.dependencies import Permissions
from src.common.services.crypto.crypto_service import EncryptionService
from src.modules.codes.code_service import CodeService
from src.common.services.jwt.jwt_service import JwtService
from src.modules.auth.mappers.auth_mappers import (
    map_to_jwt_response,
    map_to_message_response,
)
from src.modules.users.user_service import UserService
from src.common.types.types import Message, Token


class ResetPasswordService:

    def __init__(self):
        self.user_service = UserService()
        self.code_service = CodeService()
        self.encryption_service = EncryptionService()
        self.jwt_service = JwtService()

    def start(self, email: str) -> Token:
        user = self.user_service.get(email)

        if user is None:
            raise HTTPException(
                status_code=500,
                detail="We are sorry, an error occurred during the reset password process",
            )

        self.code_service.send(email)
        token = self.jwt_service.encode(
            {"sub": email, "permissions": Permissions.RESET_PASSWORD.value},
            expiration_time=2,
        )

        return map_to_jwt_response(token)

    def verify(self, email: str, code: str) -> Message:
        is_verified = self.code_service.validate(email, code)

        if not is_verified:
            raise HTTPException(status_code=400, detail="Invalid verification attempt")

        return map_to_message_response("Code verified successfully")

    def finish(self, email: str, new_password: str) -> Message:
        has_active_code = self.code_service.is_active(email)

        if not has_active_code:
            raise HTTPException(
                status_code=400,
                detail="You must verify your code before changing your password",
            )

        password_hash = self.encryption_service.encrypt(new_password)
        self.user_service.update(email, {"password": password_hash})

        return map_to_message_response("Password updated successfully")
