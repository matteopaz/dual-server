"""Application API routes."""

from fastapi import APIRouter

root_router = APIRouter()

@root_router.get("/ping", summary="Service health probe")
async def pong() -> dict[str, str]:
    """Return a simple heartbeat response."""
    return {"message": "pong"}
