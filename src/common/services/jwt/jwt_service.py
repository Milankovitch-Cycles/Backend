import jwt
from typing import Any
from fastapi import HTTPException
from src.common.services.jwt.mappers.jwt_mapper import map_to_payload
from settings import JWT_ALGORITHM, JWT_EXPIRES_IN, JWT_SECRET


class JwtService:
    def __init__(self):
        self.secret = JWT_SECRET
        self.algorithm = JWT_ALGORITHM

    def encode(self, data, expiration_time=JWT_EXPIRES_IN) -> str:
        return jwt.encode(
            payload=map_to_payload(data, expiration_time),
            key=self.secret,
            algorithm=self.algorithm,
        )

    def decode(self, token) -> Any:
        try:
            return jwt.decode(jwt=token, key=self.secret, algorithms=self.algorithm)
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail="Token has expired")
        except jwt.InvalidTokenError:
            raise HTTPException(status_code=401, detail="Invalid token")
