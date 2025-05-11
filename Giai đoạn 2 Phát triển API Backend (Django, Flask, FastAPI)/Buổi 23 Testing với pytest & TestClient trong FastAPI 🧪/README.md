# Buổi 23: Testing với pytest & TestClient trong FastAPI 🧪

### 1. Cài đặt
```bash
pip install pytest pytest-asyncio httpx
```
- pytest: test runner

- pytest-asyncio: hỗ trợ test async

- httpx: TestClient sử dụng client HTTP

Tạo file cấu hình cơ bản `pytest.ini`:
```ini
[pytest]
asyncio_mode = auto
python_files = tests/test_*.py
```
### 2. Tạo fixture app & client
Trong thư mục `tests/`, thêm `conftest.py`:
```python
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
```
- scope="module": fixture chạy một lần cho toàn module test.

### 3. Viết test cho endpoint đơn giản
Tạo file `tests/test_health.py`:
```python
# tests/test_health.py
def test_health_check(test_client):
    response = test_client.get("/health/")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
```
### 4. Test CRUD Books (bao gồm cache)
Giả sử bạn có router `/books/` với cache Redis. Bạn có thể mock Redis client để không phụ thuộc service thật.

Trong `tests/conftest.py` thêm:
```python
from unittest.mock import MagicMock
import app.db.redis_sync as redis_mod

@pytest.fixture(autouse=True)
def mock_redis(monkeypatch):
    fake = MagicMock()
    # get -> None để test lần đầu cache miss
    fake.get.return_value = None
    monkeypatch.setattr(redis_mod, "get_redis_client", lambda: fake)
    return fake
```
Test CRUD:
```python
# tests/test_books.py
import json

def test_get_books_empty(test_client):
    # ban đầu list_books trả []
    resp = test_client.get("/books/")
    assert resp.status_code == 200
    assert resp.json() == []

def test_create_and_get_book(test_client, mock_redis):
    # Tạo book
    payload = {"title": "A", "author": "B"}
    resp = test_client.post("/books/", json=payload)
    assert resp.status_code == 201
    book = resp.json()
    assert book["title"] == "A"
    assert book["author"] == "B"

    # Sau khi tạo, cache.delete("books_all") đã được gọi
    mock_redis.delete.assert_called_with("books_all")

    # Lấy lại list_books: lần này dữ liệu trong DB (in-memory)
    resp2 = test_client.get("/books/")
    assert resp2.status_code == 200
    assert isinstance(resp2.json(), list)
    assert any(b["title"] == "A" for b in resp2.json())
```
### 5. Test Authentication & Protected Route
Tạo user trước, đăng nhập, dùng token để test:  
```python
# tests/test_auth.py
def test_register_and_login_and_me(test_client):
    # Register
    resp1 = test_client.post("/auth/register", json={"username":"u1","password":"pass"})
    assert resp1.status_code == 200

    # Login
    resp2 = test_client.post("/auth/login", json={"username":"u1","password":"pass"})
    assert resp2.status_code == 200
    token = resp2.json()["access_token"]

    # Truy cập /users/me
    headers = {"Authorization": f"Bearer {token}"}
    resp3 = test_client.get("/users/me", headers=headers)
    assert resp3.status_code == 200
    data = resp3.json()
    assert data["username"] == "u1"
```
Test trường hợp token sai:
```python
def test_me_unauthorized(test_client):
    resp = test_client.get("/users/me")
    assert resp.status_code == 401
```
### 6. Test Async Endpoint (FastAPI) với pytest-asyncio
Nếu bạn có endpoint async trong router `/books_async/`:
```python
# tests/test_async.py
import pytest

@pytest.mark.asyncio
async def test_get_books_async(monkeypatch):
    from app.db.redis_async import get_redis_pool
    fake = MagicMock()
    fake.get.return_value = None
    monkeypatch.setattr("app.db.redis_async.get_redis_pool", lambda: fake)

    from httpx import AsyncClient
    from app.main import app

    async with AsyncClient(app=app, base_url="http://test") as ac:
        resp = await ac.get("/books_async/")
        assert resp.status_code == 200
```
### 7. Chạy test & Coverage
```bash
pytest --maxfail=1 --disable-warnings -q
# Nếu muốn đo coverage:
pip install pytest-cov
pytest --cov=app tests/
```
📋 Bài tập
1. Viết test cho RabbitMQ producer: mock send_message để xác nhận background_tasks.add_task được gọi.

2. Test endpoint cache Memcached: mock client tương tự Redis.

3. Tạo fixture DB tạm (sqlite in-memory) để test các CRUD SQLAlchemy mà không ảnh hưởng DB thật.

4. Thiết lập test cho các validator Pydantic: đưa data invalid và assert ra lỗi 422.