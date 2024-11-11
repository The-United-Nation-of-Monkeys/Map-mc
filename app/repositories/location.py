from sqlalchemy import insert, select, delete

from app.db.config import async_session_factory
from app.db.models.location import Location
from app.schemas.location import SBaseLocation



async def get_location_info_db(location_id):
    async with async_session_factory() as session:
        query = select(Location.__table__.columns).where(Location.id ==location_id)
        location = await session.execute(query)
        location_info = location.mappings().first()
        
        return location_info
    
async def add_location_db(location_info: SBaseLocation):
    async with async_session_factory() as session:
        query = insert(Location).values(**location_info.model_dump())
        await session.execute(query)
        await session.commit()
        
async def get_all_locations_db():
    async with async_session_factory() as session:
        query = select(Location)
        locations = await session.execute(query)
        locations_info = locations.scalars().all()
        
        return locations_info
    
async def delete_location_db(id: int):
    async with async_session_factory() as session:
        query = delete(Location).where(Location.id == id)
        await session.execute(query)
        await session.commit()