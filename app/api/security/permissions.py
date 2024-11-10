from sqlalchemy import select
from functools import wraps
from fastapi import Request

from app.api.security.token import decode

def check_permissions(role: str):
    def decorator(func):
        @wraps
        async def wrapper(*args, **kwargs):
            token: str = kwargs.get("token")
            try:
                token_info = decode(token)
            
            except Exception:
                pass
