from fastapi import FastAPI

from app.api.map import router as router_map

app = FastAPI(
    openapi_prefix="/api/v1"
)

app.include_router(router_map)
