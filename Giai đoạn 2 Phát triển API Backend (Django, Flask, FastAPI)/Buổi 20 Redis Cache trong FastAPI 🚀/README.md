# Buổi 20: Redis Cache trong FastAPI 🚀
### 1. Chuẩn bị môi trường
#### A. Cài Docker (nếu chưa có)
```bash
# Kéo image Redis và chạy container
docker run -d --name redis-cache -p 6379:6379 redis:7
```
#### B. Cài thư viện Python
Trong virtualenv:
```bash
pip install redis fastapi uvicorn
# hoặc nếu muốn async:
pip install aioredis
```
### 2. Kết nối Redis trong FastAPI
#### A. Synchronous với redis-py
```Python
# app/db/redis_sync.py
import redis
from functools import lru_cache

@lru_cache()
def get_redis_client():
    return redis.Redis(host="localhost", port=6379, decode_responses=True)
```
#### B. Asynchronous với aioredis
```Python
# app/db/redis_async.py
import aioredis
from functools import lru_cache

@lru_cache()
def get_redis_pool():
    return aioredis.from_url("redis://localhost:6379", encoding="utf-8", decode_responses=True)
```
### 3. Caching trong endpoint
Giả sử bạn có API lấy sách từ database tốn thời gian, ta sẽ cache kết quả trong Redis.
#### A. Ví dụ synchronous
```Python 
# app/routers/books.py
from fastapi import APIRouter, Depends
from typing import List
from .schemas import BookOut
from .services.book_service import list_books
from db.redis_sync import get_redis_client
import json

router = APIRouter(prefix="/books", tags=["books"])

@router.get("/", response_model=List[BookOut])
def get_books(cache: redis.Redis = Depends(get_redis_client)):
    # Thử lấy từ cache
    cached = cache.get("books_all")
    if cached:
        return json.loads(cached)

    # Nếu không có, gọi service và lưu vào cache
    data = list_books()
    result = [b.dict() for b in data]
    cache.set("books_all", json.dumps(result), ex=60)  # TTL = 60s
    return result
```
#### B. Ví dụ asynchronous
```Python
# app/routers/books_async.py
from fastapi import APIRouter, Depends
from typing import List
from .schemas import BookOut
from .services.book_service import list_books
from db.redis_async import get_redis_pool
import json

router = APIRouter(prefix="/books_async", tags=["books_async"])

@router.get("/", response_model=List[BookOut])
async def get_books(cache=Depends(get_redis_pool)):
    cached = await cache.get("books_all_async")
    if cached:
        return json.loads(cached)

    data = list_books()
    result = [b.dict() for b in data]
    await cache.set("books_all_async", json.dumps(result), ex=120)  # TTL = 2 phút
    return result
```
### 4. Invalidating Cache
Khi dữ liệu thay đổi (POST/PUT/DELETE), phải xóa hoặc cập nhật cache:
```Python 
@router.post("/", status_code=201)
def create_book(book_in: BookIn, cache: redis.Redis = Depends(get_redis_client)):
    new = create_book_service(book_in)
    # Xóa cache cũ
    cache.delete("books_all")
    return new
```
## 📋 Bài tập
1. Cache chi tiết sách theo ID
- Endpoint `GET /books/{id}`: cache riêng cho từng `id` với key `"book_{id}"` và TTL = 300s.
2. Invalidation
- Khi gọi `PUT /books/{id}` hoặc `DELETE /books/{id}`, xóa cache `"book_{id}"` và `"books_all"`.
3. Async cache
- Triển khai lại cả hai endpoint trên (`GET all` & `GET by id`) sử dụng `aioredis`.