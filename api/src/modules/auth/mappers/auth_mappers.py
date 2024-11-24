from src.common.entities.user_entity import UserEntity
from src.modules.auth.dtos.dtos import GetUserDto
from src.common.types.types import Message, Token


def map_to_message_response(message: str) -> Message:
    return Message(message=message)


def map_to_jwt_response(token: str) -> Token:
    return Token(type="bearer", access_token=token)

def map_to_user_dto(user: UserEntity) -> GetUserDto:
    return GetUserDto(
        pic=user.pic,
        first_name=user.first_name,
        last_name=user.last_name,
        email=user.email,
    )