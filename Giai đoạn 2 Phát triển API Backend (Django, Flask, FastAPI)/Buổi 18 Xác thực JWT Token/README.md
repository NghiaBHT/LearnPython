# 🛡️ Buổi 18: Xác thực JWT Token trong FastAPI
### 1. Cài thư viện hỗ trợ
```bash
pip install python-jose[cryptography] passlib[bcrypt]
```
### 2. Cấu hình JWT
```Python
# app/core/security.py
from datetime import datetime, timedelta
from jose import JWTError, jwt

SECRET_KEY = "secret-key-cua-ban"  # nên để trong .env
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload.get("sub")
    except JWTError:
        return None
```

### 3. Hash mật khẩu & model người dùng
``` Python
# app/core/hash.py
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)
```

### 4. Định nghĩa Pydantic Schema
``` Python
# app/schemas/auth.py
from pydantic import BaseModel

class UserLogin(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
```

### 5. Đăng ký người dùng
```Python
# app/routers/auth.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.database import get_db
from db import models
from core.hash import hash_password
from schemas.auth import UserLogin
from schemas.user import UserOut

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register", response_model=UserOut)
def register(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.username == user.username).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    new_user = models.User(
        username=user.username,
        email=f"{user.username}@example.com",
        password=hash_password(user.password),
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
```
### 6. Đăng nhập & Trả JWT
```Python
from core.security import create_access_token
from core.hash import verify_password
from schemas.auth import Token

@router.post("/login", response_model=Token)
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.username == user.username).first()
    if not db_user or not verify_password(user.password, db_user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_access_token({"sub": db_user.username})
    return {"access_token": token, "token_type": "bearer"}
```
### 7. Bảo vệ API với `OAuth2PasswordBearer`
```python
# app/core/dependencies.py
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from core.security import verify_token
from db.database import get_db
from db import models
from sqlalchemy.orm import Session

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    username = verify_token(token)
    if not username:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    user = db.query(models.User).filter(models.User.username == username).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
```
### 8. Sử dụng `get_current_user` trong API
```Python
# app/routers/user.py
from fastapi import APIRouter, Depends
from core.dependencies import get_current_user
from schemas.user import UserOut

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/me", response_model=UserOut)
def get_me(current_user = Depends(get_current_user)):
    return current_user
```
### 📋 Bài tập
1. Viết API `/auth/register` để người dùng đăng ký.

2. Viết API `/auth/login` để trả JWT token.

3. Viết API `/users/me` để trả thông tin user đang đăng nhập.

4. Gửi request bằng Postman hoặc curl với Bearer token để test `/users/me`.
