# tests/conftest.py
import pytest
from fastapi.testclient import TestClient
from app.main import app  # import app từ app/main.py

@pytest.fixture(scope="module")
def test_client():
    # Khởi TestClient
    client = TestClient(app)
    yield client
    # cleanup nếu cần