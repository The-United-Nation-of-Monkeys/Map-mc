from fastapi import APIRouter, status, Depends
from fastapi.security import HTTPBearer, HTTPBasicCredentials
from typing import Annotated

from app.repositories.location import get_location_info, add_location
from app.api.errors import error_404
from app.schemas.location import SLocationInfo, SBaseLocation
from app.config import security

router = APIRouter(
    prefix="/map",
    tags=["Map"]
)


@router.get("/{location}")
async def get_location(location: str):
    return "sosi huy"


@router.get("/info/{location_id}")
async def get_info(location_id: int):
    location = await get_location_info(location_id)
    
    if not location:
        error_404()
        
    return SLocationInfo(location)


@router.post("/add/location", status_code=status.HTTP_204_NO_CONTENT)
async def add_location(location_info: SBaseLocation, token: Annotated[HTTPBasicCredentials, Depends(security)]):
    await add_location(location_info)
    
    