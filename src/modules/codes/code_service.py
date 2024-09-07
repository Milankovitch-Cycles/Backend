from src.common.services.smtp.smtp_service import SmtpService
from src.common.entities.code_entity import CodeEntity
from sqlalchemy.orm import Session
import random


class CodeService:
    def __init__(self, session: Session):
        self.session = session
        self.smtp_service = SmtpService()

    def create(self, email: str) -> str:
        code_entity = CodeEntity(
            code=str(random.randrange(100000, 999999)), email=email
        )
        self.session.add(code_entity)
        self.session.commit()

        return code_entity.code

    def send(self, email: str):
        code = self.create(email)
        return self.smtp_service.send_email(
            email, "Verification Code", f"Your code is {code}"
        )
