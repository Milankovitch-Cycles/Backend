from typing import Optional
from pydantic import BaseModel


class LoginRequestDto(BaseModel):
    email: str
    password: str


class StartRegistrationRequestDto(BaseModel):
    email: str
    password: str
    first_name: str
    last_name: str


class FinishRegistrationRequestDto(BaseModel):
    code: str


class InitResetPasswordDto(BaseModel):
    email: str


class VerifyResetPasswordDto(BaseModel):
    code: str


class FinishResetPasswordDto(BaseModel):
    password: str

class GetUserDto(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    pic: Optional[str] = None
    email: Optional[str] = None