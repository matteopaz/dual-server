"""Application factory and ASGI entrypoint."""

from fastapi import FastAPI

from .api import router


def create_app() -> FastAPI:
    """Build and configure the FastAPI application instance."""
    app = FastAPI()
    app.include_router(router)
    return app


app = create_app()

__all__ = ("app", "create_app")
