# Buổi 11: Xây dựng cấu trúc Flask chuẩn MVC
1. Cấu trúc thư mục mẫu
```
api_project/
│
├── src/
│   ├── app/
│   │   ├── __init__.py          # Factory tạo app, đăng ký Blueprint
│   │   ├── config.py            # Cấu hình (Dev/Prod/Test)
│   │   │
│   │   ├── models/              # Mô hình dữ liệu (SQLAlchemy)
│   │   │   ├── __init__.py
│   │   │   └── book.py
│   │   │
│   │   ├── controllers/         # Xử lý logic & route handlers
│   │   │   ├── __init__.py
│   │   │   └── book_controller.py
│   │   │
│   │   ├── schemas/             # Định nghĩa Pydantic hoặc Marshmallow schemas (tuỳ chọn)
│   │   │   ├── __init__.py
│   │   │   └── book_schema.py
│   │   │
│   │   └── extensions.py        # Khởi tạo các extension (db, migrate,…)
│   │
│   ├── migrations/              # Flask-Migrate (Alembic) scripts
│   └── manage.py                # CLI entry point (run, migrate,…)
│
├── requests/
│   └── books.http               # bộ request để test API
│
├── .env                         # biến môi trường (SECRET_KEY, DB_URI…)
├── requirements.txt
└── README.md
```
2. Khởi tạo và chạy
- Cài các thư viện cần thiết
```
pip install flask flask_sqlalchemy flask_migrate flask_script
pip freeze > requirements.txt
```
- Khởi tạo migrations
```
cd src
python manage.py db init
python manage.py db migrate -m "Initial migration"
python manage.py db upgrade
```
- Chạy app
```
export FLASK_ENV=development
python manage.py runserver
```