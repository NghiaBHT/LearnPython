# Buổi 14: Tổ chức cấu trúc folder & Sử dụng Routers trong FastAPI
1. Cấu trúc thư mục gợi ý
```
api_project/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── routers/
│   │   ├── __init__.py
│   │   ├── health.py
│   │   ├── books.py
│   │   └── users.py
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── book.py
│   │   └── user.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── book_service.py
│   │   └── user_service.py
│   └── models/                # (tùy chọn nếu có ORM)
│       ├── __init__.py
│       └── book_model.py
│
├── tests/                     # (sau này) test modules
│
├── requirements.txt
└── README.md
```
- `app/main.py`: entry point, khởi tạo FastAPI() và mount các router
- `app/config.py`: cấu hình chung (port, debug, DB URL…)
- `app/routers/`: chứa các module router, mỗi file là một nhóm endpoint
- `app/schemas/`: Pydantic models cho requests/responses
- `app/services/`: logic nghiệp vụ, interface với DB hoặc lưu trữ tạm
- `app/models/`: nếu dùng ORM (SQLAlchemy, Tortoise…), định nghĩa entity

2. Chạy ứng dụng
    ```
    uvicorn app.main:app --reload
    ```
    - Đường dẫn sẽ là:
        - `GET /health/`
        - `GET /books/`
        - `POST /books/`
        - `GET /users/{username}`
    - Swagger UI tự động gom các endpoint theo tags bạn khai báo:
        http://localhost:8000/docs

3. Ưu điểm của cách tổ chức này
    - Tách biệt rõ ràng giữa phần định nghĩa schema, business logic, và routing
    - Dễ mở rộng: mỗi resource (books, users…) có `folder/router` riêng
    - Dễ test: bạn có thể import trực tiếp các service để viết unit test mà không cần khởi server