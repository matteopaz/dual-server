"""Shared pytest fixtures."""

from collections.abc import Iterator

import pytest
from fastapi.testclient import TestClient

from app import app


@pytest.fixture()
def client() -> Iterator[TestClient]:
    """Yield a FastAPI TestClient bound to the application."""
    with TestClient(app) as test_client:
        yield test_client
