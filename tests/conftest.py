import pytest
from fastapi.testclient import TestClient
from app.main import app  # Import FastAPI app

@pytest.fixture(scope="module")
def test_client():
    """Fixture to provide a test client."""
    client = TestClient(app)
    yield client  # Provide test client instance
