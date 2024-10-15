import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

JWT_SECRET = os.environ.get("JWT_SECRET")
JWT_ALGORITHM = os.environ.get("JWT_ALGORITHM")
JWT_EXPIRES_IN = int(os.environ.get("JWT_EXPIRES_IN"))

CIPHER_KEY = os.environ.get("CIPHER_KEY")

SENDER_NAME = os.environ.get("SENDER_NAME")
SENDER_EMAIL = os.environ.get("SENDER_EMAIL")
SENDER_PASSWORD = os.environ.get("SENDER_PASSWORD")

SMTP_SERVER = os.environ.get("SMTP_SERVER")
SMTP_PORT = int(os.environ.get("SMTP_PORT"))

DATABASE_URL = os.environ.get("DATABASE_URL")
