from fastapi import FastAPI

from app.core.config import settings
from app.api.v1.router import api_router
app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
)
app.include_router(api_router)

@app.get("/")
def root():
    return {
        "message": "AI Study Assistant API is running",
        "environment": settings.environment,
        "version": settings.app_version,
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
    }