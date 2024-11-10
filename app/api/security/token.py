
import datetime, jwt

from app.config import settings


async def decode(
    token: str | bytes,
    key = settings.auth.public_key.read_text(),
    algorithm = settings.auth.algorithm
):
    return jwt.decode(token, key, algorithm)

