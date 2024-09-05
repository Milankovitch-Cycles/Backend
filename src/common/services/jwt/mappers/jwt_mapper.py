import datetime
from src.common.services.jwt.types.jwt_types import JwtPayload


def map_to_payload(message, expiration_time) -> JwtPayload:
    return {
        "iat": datetime.datetime.now(datetime.UTC),
        "exp": datetime.datetime.now(datetime.UTC)
        + datetime.timedelta(seconds=expiration_time),
        "sub": message,
    }
