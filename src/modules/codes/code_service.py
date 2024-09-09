import datetime
from fastapi import HTTPException
from src.common.services.smtp.smtp_service import SmtpService
from src.common.entities.code_entity import CodeEntity
from sqlalchemy.orm import Session
import random


class CodeService:
    def __init__(self, session: Session):
        self.session = session
        self.smtp_service = SmtpService()

    def create_code(self, email: str) -> str:
        code_entity = CodeEntity(
            code=str(random.randrange(100000, 999999)), email=email
        )
        self.session.add(code_entity)
        self.session.commit()

        return code_entity.code

    def send_code(self, email: str):
        code = self.create_code(email)
        return self.smtp_service.send_email(
            email, "Verification Code", f"Your code is {code}"
        )

    def get_by_email(self, email: str) -> CodeEntity:
        return (
            self.session.query(CodeEntity)
            .filter(CodeEntity.email == email)
            .order_by(CodeEntity.created_at.desc())
            .first()
        )

    def validate_code(self, email: str, code: str) -> bool:
        last_code = self.get_by_email(email)

        if (
            last_code is None
            or last_code.code != code
            or last_code.created_at
            < datetime.datetime.now() - datetime.timedelta(seconds=60)
        ):
            return False

        last_code.verified = True
        self.session.add(last_code)
        self.session.commit()

        return True

    def has_active_code(self, email: str) -> bool:
        last_code = self.get_by_email(email)

        if (
            last_code is None
            or not last_code.verified
            or last_code.created_at
            < datetime.datetime.now() - datetime.timedelta(seconds=60)
        ):
            return False

        return True
