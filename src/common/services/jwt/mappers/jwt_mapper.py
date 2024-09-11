import datetime


def map_to_payload(data, expiration_time):
    payload = {
        "iat": datetime.datetime.now(datetime.UTC),
        "exp": datetime.datetime.now(datetime.UTC)
        + datetime.timedelta(minutes=expiration_time),
    }
    payload.update(data)
    return payload
