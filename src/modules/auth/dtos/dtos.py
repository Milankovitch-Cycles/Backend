from pydantic import BaseModel


class LoginRequestDto(BaseModel):
    email: str
    password: str


class StartRegistrationRequestDto(BaseModel):
    email: str
    password: str


class FinishRegistrationRequestDto(BaseModel):
    code: str


class InitResetPasswordDto(BaseModel):
    email: str


class VerifyResetPasswordDto(BaseModel):
    code: str


class FinishResetPasswordDto(BaseModel):
    password: str
