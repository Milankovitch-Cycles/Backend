def map_to_register_response():
    return {"message": "User created successfully"}


def map_to_login_response(token: str):
    return {"Authorization": f"Bearer { token }"}
