# LearnPythonBuổi 21: Kết nối Memcached trong FastAPI 🏷️
### 1. Giới thiệu Memcached
- Là hệ thống cache in-memory nhẹ, đơn giản, chỉ lưu key→value

- Phù hợp cho caching nhanh, không hỗ trợ phức tạp như Redis (không có list, set, pub/sub…)

- Dùng khi bạn cần cache tạm, không cần persistence hay các data structure nâng cao

### 2. Khởi chạy Memcached với Docker
```bash
docker run -d --name memcached-cache -p 11211:11211 memcached:latest
```
| Mặc định Memcached lắng nghe cổng 11211

### 3. Cài thư viện Python
```bash
pip install pymemcache
```
### 4. Kết nối Memcached trong FastAPI
#### A. Tạo client Memcached
```python
# app/db/memcached_client.py
from pymemcache.client.base import Client
from functools import lru_cache

@lru_cache()
def get_memcached_client() -> Client:
    return Client(('localhost', 11211), serde=None)
```
#### B. Ví dụ sử dụng cache
Giả sử có `service list_users()` trả về danh sách user, ta cache bằng Memcached:
```Python
# app/routers/users.py
from fastapi import APIRouter, Depends
from typing import List
from app.schemas.user import UserOut
from app.services.user_service import list_users
from app.db.memcached_client import get_memcached_client
import json

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/", response_model=List[UserOut])
def get_users(cache = Depends(get_memcached_client)):
    key = "users_all"
    cached = cache.get(key)
    if cached:
        # pymemcache trả bytes
        return json.loads(cached.decode('utf-8'))

    users = list_users()
    result = [u.dict() for u in users]
    cache.set(key, json.dumps(result), expire=60)  # TTL 60s
    return result
```

### 6. Bài tập
1. Cache chi tiết user theo ID
- Endpoint `GET /users/{id}`: cache riêng với key `"user_{id}"`, TTL 120s.

2. Invalidation
- Khi `PUT /users/{id}` hoặc `DELETE /users/{id}`: xóa cache `"user_{id}"` và `"users_all"`.

3. Sử dụng Memcached
- Triển khai cả `GET all` và `GET by id` users với Memcached.