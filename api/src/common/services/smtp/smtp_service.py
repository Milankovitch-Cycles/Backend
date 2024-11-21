import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import Optional
from settings import SENDER_EMAIL, SENDER_NAME, SENDER_PASSWORD, SMTP_PORT, SMTP_SERVER
from pydantic import BaseModel


class Sender(BaseModel):
    email: str
    name: Optional[str]
    password: Optional[str]


class Server(BaseModel):
    hostname: str
    port: int


class SmtpService:
    def __init__(self):
        self.sender = Sender(
            name=SENDER_NAME, email=SENDER_EMAIL, password=SENDER_PASSWORD
        )
        self.server = Server(hostname=SMTP_SERVER, port=SMTP_PORT)

    def create_body(self, sender: Sender, receiver: str, title: str, text: str) -> str:
        message = MIMEMultipart("alternative")
        message["Subject"] = title
        message["From"] = f"{sender.name} <{sender.email}>"
        message["To"] = receiver

        html_template = f"""
        <html>
            <body style="font-family: Arial, sans-serif; margin: 0; padding: 50px; background-color: #f5f6f1;">
                <div style="max-width: 600px; margin: 50px auto; background-color: #ffffff; border-radius: 8px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); overflow: hidden;">
                    <div style="background-color: #0077b6; color: #ffffff; padding: 20px; text-align: center;">
                        <h1 style="margin: 0; font-size: 24px;">Milankovic API</h1>
                        <p style="margin: 5px 0 0; font-size: 16px;">{title}</p>
                    </div>
                    <div style="padding: 20px;">
                        <p style="font-size: 16px; color: #333333; line-height: 1.6;">
                            {text}
                        </p>
                    </div>
                    <div style="background-color: #f4f4f4; color: #777777; padding: 10px; text-align: center; font-size: 12px;">
                        © 2024 Milankovic API. Todos los derechos reservados.
                    </div>
                </div>
            </body>
        </html>
        """

        message.attach(MIMEText(html_template, "html"))

        return message.as_string()

    def send_email(self, receiver: str, title: str, text: str):
        body = self.create_body(self.sender, receiver, title, text)

        try:
            with smtplib.SMTP_SSL(self.server.hostname, self.server.port) as server:
                server.login(self.sender.email, self.sender.password)
                server.sendmail(self.sender.email, receiver, body)
        except Exception as e:
            print(f"There was an error with the request to SMTP API: {e}")
