from sqlalchemy.orm import Mapped, mapped_column
from app.db.config import Base

class Location(Base):
    __tablename__ = "location"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)
    sector: Mapped[str | None]
    description: Mapped[str | None]
    type: Mapped[str]