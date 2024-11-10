from pydantic import BaseModel



class SBaseLocation(BaseModel):
    name: str
    sector: str | None = None
    description: str | None = None
    type: str 
    
    
class SLocationInfo(BaseModel, SBaseLocation):
    id: set
    