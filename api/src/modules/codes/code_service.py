import datetime
from src.common.services.smtp.smtp_service import SmtpService
from src.common.entities.code_entity import CodeEntity
from src.common.config.config import session
import random


class CodeService:
    def __init__(self):
        self.smtp_service = SmtpService()

    def get(self, email: str) -> CodeEntity:
        return (
            session.query(CodeEntity)
            .filter(CodeEntity.email == email)
            .order_by(CodeEntity.created_at.desc())
            .first()
        )

    def create(self, email: str) -> str:
        random_code = str(random.randrange(100000, 999999))
        code_entity = CodeEntity(code=random_code, email=email)
        session.add(code_entity)
        session.commit()
        return code_entity.code

    def send(self, email: str):
        code = self.create(email)
        return self.smtp_service.send_email(
            email, "Verification Code", f"Your code is {code}"
        )

    def validate(self, email: str, code: str) -> bool:
        last_code = self.get(email)

        if (
            last_code is None
            or last_code.code != code
            or last_code.created_at
            < datetime.datetime.now() - datetime.timedelta(seconds=60)
        ):
            return False

        last_code.verified = True
        session.add(last_code)
        session.commit()

        return True

    def is_active(self, email: str) -> bool:
        last_code = self.get(email)

        if (
            last_code is None
            or not last_code.verified
            or last_code.created_at
            < datetime.datetime.now() - datetime.timedelta(seconds=60)
        ):
            return False

        return True
