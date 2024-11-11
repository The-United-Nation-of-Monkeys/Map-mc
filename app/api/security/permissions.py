from sqlalchemy import select
from functools import wraps
from fastapi import Request

from app.api.security.token import decode
from app.api.errors import error_401, error_403

def permissions(role: str):
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            token: str = kwargs.get("token")
            
            try:
                payload = await decode(token.credentials)
            except Exception as e:
                print(e)
                error_401()
                
            if payload.get("role") != role:
                error_403()
            
            return await func(*args, **kwargs)    
        return wrapper
    return decorator
