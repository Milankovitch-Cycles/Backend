from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from requests import Session

from src.common.config.config import get_db
from src.modules.auth.auth_service import AuthService


def get_auth_service(session: Session = Depends(get_db)):
    return AuthService(session)


def get_user_in_reset_password_flow(  # TO-DO: Add decorator to get_current_user
    db: Session = Depends(get_db),
    token: str = Depends(OAuth2PasswordBearer(tokenUrl="/auth/login")),
):
    auth_service = AuthService(db)
    return auth_service.get_user_in_reset_password_flow(token)


def get_user(
    db: Session = Depends(get_db),
    token: str = Depends(OAuth2PasswordBearer(tokenUrl="/auth/login")),
):
    auth_service = AuthService(db)
    return auth_service.get_user_in_session(token)
