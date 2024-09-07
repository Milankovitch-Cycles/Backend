import smtplib
from email.mime.text import MIMEText
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
        self.sender = Sender(name=SENDER_NAME, email=SENDER_EMAIL, password=SENDER_PASSWORD)
        self.server = Server(hostname=SMTP_SERVER, port=SMTP_PORT)
        
    def create_body(self, sender: Sender, receiver: str, title: str, text: str) -> str:
        body = MIMEText(text)
        body["Subject"] = title
        body["From"] = f"{sender.name} <{sender.email}>"
        body["To"] = receiver
        
        return body.as_string()
        
    def send_email(self, receiver: str, title: str, text: str):        
        body = self.create_body(self.sender, receiver, title, text)
        
        with smtplib.SMTP_SSL(self.server.hostname, self.server.port) as server:
            server.login(self.sender.email, self.sender.password)
            server.sendmail(self.sender.email, receiver, body)
            
        
