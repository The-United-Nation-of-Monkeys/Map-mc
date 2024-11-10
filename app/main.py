from fastapi import FastAPI

app = FastAPI(
    openapi_prefix="/api/v1"
)

@app.get("/map/{location}")
async def get_location(location: str):
    return "sosi huy"