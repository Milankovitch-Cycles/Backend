from pydantic import BaseModel


class RegisterRequestDto(BaseModel):
    email: str
    password: str
