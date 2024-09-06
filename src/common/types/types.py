from pydantic import BaseModel

class Message(BaseModel):
    message: str
    
class Token(BaseModel):
    type: str
    access_token: str