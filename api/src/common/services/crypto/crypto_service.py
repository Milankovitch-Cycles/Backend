from cryptography.fernet import Fernet

from settings import CIPHER_KEY


class EncryptionService:
    def __init__(self):
        self.cipher = Fernet(CIPHER_KEY.encode())

    def encrypt(self, plaintext: str) -> str:
        return self.cipher.encrypt(plaintext.encode()).decode()

    def decrypt(self, ciphertext: str) -> str:
        return self.cipher.decrypt(ciphertext.encode()).decode()
