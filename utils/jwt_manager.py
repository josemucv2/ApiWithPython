from jwt import encode, decode


def generate_token(data: dict) -> str:
    token: str = encode(payload=data, key="my_token", algorithm="HS256")
    return token


def validate_token(token: str) -> dict:
    data = decode(token, key="my_token", algorithms=['HS256'])

    return data
