from fastapi import HTTPException
from src.modules.auth.dtos.dtos import StartRegistrationRequestDto
from src.common.entities.user_entity import UserEntity
from src.modules.auth.dependencies.dependencies import Permissions
from src.common.services.jwt.jwt_service import JwtService
from src.modules.codes.code_service import CodeService
from src.common.services.hash.hash_service import HashService
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
        self.hash_service = HashService()
        self.jwt_service = JwtService()

    def start(self, request: StartRegistrationRequestDto) -> Token:
        user = self.user_service.get_by_email(request.email)

        if user:
            raise HTTPException(
                status_code=409,
                detail="We are sorry, an error occurred during the registration process",
            )

        hashed_password = self.hash_service.hash(request.password)
        token = self.jwt_service.encode(
            {
                "email": request.email,
                "password": hashed_password,
                "first_name": request.first_name,
                "last_name": request.last_name,
                "permissions": Permissions.REGISTER.value,
            },
            expiration_time=1,
        )
        self.code_service.send(request.email)

        return map_to_jwt_response(token)

    def finish(self, userIntent: UserEntity, code: str) -> Message:
        user = self.user_service.get_by_email(userIntent.email)

        if user:
            raise HTTPException(
                status_code=409,
                detail="We are sorry, an error occurred during the registration process",
            )

        is_verified = self.code_service.validate(userIntent.email, code)

        if not is_verified:
            raise HTTPException(
                status_code=409,
                detail="We are sorry, an error occurred during the registration process",
            )

        self.user_service.create(userIntent)

        return map_to_message_response("User created successfully")
