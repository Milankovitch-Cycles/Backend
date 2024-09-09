import datetime


def map_to_payload(message, expiration_time):
    return {
        "iat": datetime.datetime.now(datetime.UTC),
        "exp": datetime.datetime.now(datetime.UTC)
        + datetime.timedelta(minutes=expiration_time),
        "sub": message,
    }
