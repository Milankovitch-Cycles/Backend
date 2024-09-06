from fastapi import APIRouter, Depends
from src.common.config.config import get_db
from sqlalchemy.orm import Session
from .dtos.login_dto import LoginRequestDto
from .dtos.register_dto import RegisterRequestDto
from .auth_service import AuthService
from src.common.types.types import Message, Token

auth = APIRouter(tags=["Auth"], prefix="/auth")


@auth.post("/register", status_code=200, response_model=Message)
def register(register_request_dto: RegisterRequestDto, db: Session = Depends(get_db)):
    auth_service = AuthService(db)
    email, password = (register_request_dto.email, register_request_dto.password)

    return auth_service.register(email, password)


@auth.post("/login", status_code=200, response_model=Token)
def login(login_request_dto: LoginRequestDto, db: Session = Depends(get_db)):
    auth_service = AuthService(db)
    email, password = (login_request_dto.email, login_request_dto.password)

    return auth_service.login(email, password)
