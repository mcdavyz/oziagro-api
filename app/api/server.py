from fastapi import FastAPI
from app.api.routes import router

from app.config.settings import (
    API_TITLE,
    API_DESCRIPTION,
    API_VERSION,
)

app = FastAPI(
    title=API_TITLE,
    description=API_DESCRIPTION,
    version=API_VERSION,
)
app.include_router(router)

@app.get("/")
def home():
    return {
        "message": "Welcome to OziAgro DSS!"
    }