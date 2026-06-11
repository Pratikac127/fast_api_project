from datetime import datetime , timezone , timedelta
from jose import jwt , JWTError
from app.core.config import settings


def create_access_token(data: dict , expires_minute = 30):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=expires_minute)
    to_encode.update({'exp': expire })

    return jwt.encode(
        to_encode,
        settings.jwt_secret_key,
        settings.jwt_algorithm
    )


def verify_token(token):
    try:
        payload = jwt.decode(token , settings.jwt_secret_key , [settings.jwt_algorithm])

        return payload

    except JWTError:
        return None