from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title="OziAgro API",
    description="Climate Decision Support System",
    version="0.1.0"
)
app.include_router(router)

@app.get("/")
def home():
    return {
        "message": "Welcome to OziAgro DSS!"
    }