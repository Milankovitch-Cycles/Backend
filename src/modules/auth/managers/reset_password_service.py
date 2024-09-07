from fastapi import HTTPException
from requests import Session
from src.modules.codes.code_service import CodeService
from src.common.services.jwt.jwt_service import JwtService
from src.modules.auth.mappers.auth_mappers import map_to_jwt_response
from src.modules.users.user_service import UserService


class ResetPasswordService:

    def __init__(self, session: Session):
        self.user_service = UserService(session)
        self.code_service = CodeService(session)
        self.jwt_service = JwtService()

    def init(self, email: str):
        user = self.user_service.get_by_email(email)

        if user is None:
            raise HTTPException(
                status_code=500,
                detail="We are sorry, an error occurred during the reset password process.",
            )

        self.code_service.send(email)
        token = self.jwt_service.encode(email)

        return map_to_jwt_response(token)
