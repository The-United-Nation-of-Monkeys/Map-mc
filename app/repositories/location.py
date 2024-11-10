from sqlalchemy import insert, select

from app.db.config import async_session_factory
from app.db.models.location import Location
from app.schemas.location import SBaseLocation



async def get_location_info(location_id):
    async with async_session_factory() as session:
        query = select(Location).where(Location.id ==location_id)
        location = await session.execute(query)
        location_info = location.mappings.all()
        
        return location_info
    
async def add_location(location_info: SBaseLocation):
    async with async_session_factory() as session:
        query = insert(Location).values(**location_info.model_dump())
        await session.execute(query)
        await session.commit()
        