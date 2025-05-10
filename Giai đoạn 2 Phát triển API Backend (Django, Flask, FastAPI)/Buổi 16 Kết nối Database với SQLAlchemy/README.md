# Buổi 16: Kết nối Database với SQLAlchemy (FastAPI + SQLAlchemy)
## 1. Cài đặt
```
pip install sqlalchemy psycopg2-binary alembic
```
- Nếu dùng SQLite: `pip install sqlalchemy` là đủ.

## 2. Sử dụng Alembic để migration cho SQLAlchemy
### ✅ Alembic
Là công cụ migration chính thức cho SQLAlchemy.

Giúp bạn quản lý version database, thêm/sửa/xóa bảng/column mà không mất dữ liệu.

### 📦 Cài đặt Alembic
```
pip install alembic
```
### 🚀 Cách dùng Alembic (với FastAPI + SQLAlchemy)
1. Khởi tạo Alembic:
    ```
    alembic init alembic
    ```
    => Tạo folder `alembic`/ và file `alembic.ini`.
2. Cấu hình kết nối DB trong `alembic.ini`:
    ```ini
    sqlalchemy.url = sqlite:///./test.db
    # hoặc postgresql://user:password@localhost/dbname
    ```
3. Sửa env.py để import Base
    Mở `alembic/env.py`:
    ```Python
    from app.db.database import Base  # nơi bạn định nghĩa Base
    from app.db import models         # import model để Alembic "nhìn thấy"
    target_metadata = Base.metadata
    ```
4. Tạo migration mới:
    ```bash
    alembic revision --autogenerate -m "create users table"
    ```
5. Apply migration (migrate):
    ```
    alembic upgrade head
    ```

## 3. Cấu trúc thư mục khuyến nghị
```
app/
├── db/
│   ├── database.py     # kết nối DB
│   ├── models.py       # ORM classes
│   └── crud.py         # hàm CRUD
├── schemas/            # Pydantic models
│   └── user.py
├── routers/
│   └── user.py
├── main.py
```
### 3. Cấu hình kết nối DB (`database.py`)
```Python
# app/db/database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///./test.db"  # hoặc postgresql://user:pass@host/dbname

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})  # chỉ cần cho SQLite
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
```
### 4. Tạo ORM model (`models.py`)
```Python
# app/db/models.py
from sqlalchemy import Column, Integer, String
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
```

### 5. Pydantic schema (`schemas/user.py`)
```Python
from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(UserBase):
    pass

class UserOut(UserBase):
    id: int

    class Config:
        orm_mode = True
```
### 6. CRUD functions (`crud.py`)
```Python
# app/db/crud.py
from sqlalchemy.orm import Session
from . import models
from schemas.user import UserCreate

def create_user(db: Session, user: UserCreate):
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()
```
### 7. Router FastAPI (`routers/user.py`)
```Python
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db import crud, models
from db.database import SessionLocal
from schemas.user import UserCreate, UserOut

router = APIRouter(prefix="/users", tags=["users"])

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=UserOut)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)

@router.get("/{user_id}", response_model=UserOut)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
```
### 8. Tích hợp trong main.py
```Python
from fastapi import FastAPI
from db.database import Base, engine
from routers import user

# Khởi tạo DB
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Gắn router
app.include_router(user.router)
```

# ✅ Bài tập
### Bài 1: Viết thêm các hàm CRUD:
- `get_all_users`
- `update_user`
- `delete_user`
### Bài 2: Thêm bảng Post:
- `Post`: id, title, content, owner_id (ForeignKey đến `User`)
- Quan hệ one-to-many (1 User có nhiều Post)
- Tạo API tạo post và lấy post theo `user_id`