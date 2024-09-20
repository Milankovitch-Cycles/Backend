import datetime


def map_to_payload(data, expiration_time):
    payload = {
        "iat": datetime.datetime.now(),
        "exp": datetime.datetime.now()
        + datetime.timedelta(minutes=expiration_time),
    }
    payload.update(data)
    return payload
