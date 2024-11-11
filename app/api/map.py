from fastapi import APIRouter, status, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from typing import Annotated

from app.repositories.location import get_location_info_db, add_location_db, get_all_locations_db, delete_location_db
from app.api.errors import error_404
from app.schemas.location import SLocationInfo, SBaseLocation, SAllLocations
from app.config import security
from app.api.security.permissions import permissions


router = APIRouter(
    prefix="/map",
    tags=["Map"]
)


@router.get("/info/location")
async def get_info(location_id: int) -> SLocationInfo:
    location = await get_location_info_db(location_id)
    
    if not location:
        error_404()
        
    return SLocationInfo(**location)


@router.get("/info/location/all")
async def get_all_locations() -> SAllLocations:
    locations = await get_all_locations_db()
    
    return SAllLocations(locations=[SLocationInfo.model_validate(location, from_attributes=True) for location in locations])


@router.post("/add/location", status_code=status.HTTP_204_NO_CONTENT)
@permissions("student")
async def add_location(location_info: SBaseLocation, 
                       token: Annotated[HTTPAuthorizationCredentials, Depends(security)]) -> None:
    await add_location_db(location_info)
    

@router.delete("/location", status_code=status.HTTP_204_NO_CONTENT)
@permissions(role="student")
async def delete_location(location_id: int, 
                          token: Annotated[HTTPAuthorizationCredentials, Depends(security)]) -> None:
    await delete_location_db(location_id)