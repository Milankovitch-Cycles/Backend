import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

JWT_SECRET = os.environ.get("JWT_SECRET")
JWT_ALGORITHM = os.environ.get("JWT_ALGORITHM")
JWT_EXPIRES_IN = int(os.environ.get("JWT_EXPIRES_IN"))
CIPHER_KEY = os.environ.get("CIPHER_KEY")
