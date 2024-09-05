from fastapi import HTTPException
from src.common.entities.user_entity import User
from src.common.services.crypto.crypto_service import EncryptionService
from src.common.services.jwt.jwt_service import JwtService
from src.modules.auth.mappers.auth_mappers import (
    map_to_login_response,
    map_to_register_response,
)
from ..users.user_service import UserService
from sqlalchemy.orm import Session


class AuthService:
    def __init__(self, session: Session):
        self.user_service = UserService(session)
        self.encryption_service = EncryptionService()
        self.jwt_service = JwtService()

    def register(self, email: str, password: str):
        user = self.user_service.get_by_email(email)

        if user is not None:
            raise HTTPException(
                status_code=409,
                detail="We are sorry, an error occurred during the registration process.",
            )

        password_hash = self.encryption_service.encrypt(password)
        self.user_service.create(email, password_hash)

        return map_to_register_response()

    def login(self, email: str, password: str):
        user = self.user_service.get_by_email(email)

        if user is None:
            raise HTTPException(
                status_code=500,
                detail="We are sorry, an error occurred during the login process.",
            )

        decrypted_password = self.encryption_service.decrypt(user.password)

        if password != decrypted_password:
            raise HTTPException(
                status_code=500,
                detail="We are sorry, an error occurred during the login process.",
            )

        token = self.jwt_service.encode(email)

        return map_to_login_response(token)

    def verify(self, token: str) -> User:
        token = self.jwt_service.decode(token)
        user = self.user_service.get_by_email(token["sub"])

        if user is None:
            raise HTTPException(
                status_code=500,
                detail="We are sorry, an error occurred during the verification process.",
            )

        return user
