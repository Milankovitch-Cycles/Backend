from fastapi import HTTPException
from src.common.services.crypto.crypto_service import EncryptionService
from src.modules.users.user_service import UserService
from src.common.types.types import Message
from src.modules.auth.mappers.auth_mappers import (
    map_to_message_response,
)


class RegisterService:
    def __init__(self):
        self.user_service = UserService()
        self.encryption_service = EncryptionService()

    def register(self, email: str, password: str) -> Message:
        user = self.user_service.get(email)

        if user is not None:
            raise HTTPException(
                status_code=409,
                detail="We are sorry, an error occurred during the registration process",
            )

        password_hash = self.encryption_service.encrypt(password)
        self.user_service.create(email, password_hash)

        return map_to_message_response("User created successfully")
