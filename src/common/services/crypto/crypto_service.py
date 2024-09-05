from cryptography.fernet import Fernet

from settings import CIPHER_KEY


class EncryptionService:
    def __init__(self):
        key = CIPHER_KEY.encode()
        self.cipher = Fernet(key)

    def encrypt(self, plaintext: str) -> str:
        return self.cipher.encrypt(plaintext.encode()).decode()

    def decrypt(self, ciphertext: str) -> str:
        return self.cipher.decrypt(ciphertext.encode()).decode()
