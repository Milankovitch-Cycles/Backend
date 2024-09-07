from pydantic import BaseModel


class LoginRequestDto(BaseModel):
    email: str
    password: str


class RegisterRequestDto(BaseModel):
    email: str
    password: str


class InitResetPassword(BaseModel):
    email: str
