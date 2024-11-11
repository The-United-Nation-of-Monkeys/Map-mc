from pydantic import BaseModel
from dotenv import load_dotenv
from fastapi.security import HTTPBearer
from pathlib import Path
import os


BASE_DIR: Path = Path(__file__).parent.parent
load_dotenv()


class DataBase(BaseModel):
    user: str = os.environ.get("POSTGRES_USER")
    name: str = os.environ.get("POSTGRES_DB")
    password: str = os.environ.get("POSTGRES_PASSWORD")
    port: str = os.environ.get("POSTGRES_PORT")
    host: str = os.environ.get("POSTGRES_HOST")
    url: str = f"postgresql+asyncpg://{user}:{password}@{host}:{port}/{name}"
    
    
class Auth(BaseModel):
    public_key: Path = BASE_DIR / "app" / "certs" / "jwt-public.pem"
    algorithm: str = "RS256"
    
    
class Settings(BaseModel):
    db: DataBase = DataBase()
    auth: Auth = Auth()
    
    
settings = Settings()
security = HTTPBearer()