"""Application API routes."""

from fastapi import APIRouter

router = APIRouter()


@router.get("/", summary="Service health probe")
async def read_root() -> dict[str, str]:
    """Return a simple heartbeat response."""
    return {"message": "pong"}
