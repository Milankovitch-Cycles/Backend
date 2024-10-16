import hashlib

class HashService:

    def hash(self, plaintext: str) -> str:
        plaintext_bytes = plaintext.encode()
        hash = hashlib.sha256(plaintext_bytes)
        return hash.hexdigest()

