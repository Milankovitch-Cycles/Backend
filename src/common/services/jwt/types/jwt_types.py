import datetime

class JwtPayload:
    iat: datetime.datetime
    exp: datetime.datetime
    sub: str
    