from src.common.types.types import Message, Token

def map_to_message_response(message) -> Message:
    return Message(message=message)


def map_to_jwt_response(token: str) -> Token:
    return Token(type="bearer", access_token=token)
