# Buổi 19 Phân quyền, Role-based access control (RBAC)
### 1. Mô hình dữ liệu User có role
Giả sử mỗi user có 1 role: `"user"`, `"admin"`, `"moderator"`

✅ Cập nhật model User
```Python
# db/models.py
from sqlalchemy import Column, Integer, String
from db.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    role = Column(String, default="user")  # Thêm trường role
```
### 2. Mở rộng schema
```Python
# schemas/user.py
from pydantic import BaseModel

class UserOut(BaseModel):
    id: int
    username: str
    email: str
    role: str

    class Config:
        orm_mode = True
```

### 3. Gán role khi đăng ký
```Python
# routers/auth.py (trong /register)
new_user = models.User(
    username=user.username,
    email=f"{user.username}@example.com",
    password=hash_password(user.password),
    role="admin" if user.username == "admin" else "user"
)
```
### 4. Tạo middleware kiểm tra role
```Python
# core/dependencies.py
from fastapi import Depends, HTTPException, status
from core.security import verify_token
from db.database import get_db
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer
from db.models import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    username = verify_token(token)
    if not username:
        raise HTTPException(status_code=401, detail="Invalid token")
    user = db.query(User).filter(User.username == username).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

def require_role(required_roles: list[str]):
    def role_checker(current_user: User = Depends(get_current_user)):
        if current_user.role not in required_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Permission denied"
            )
        return current_user
    return role_checker
```
### 5. Sử dụng `require_role` trong route
```Python
# routers/user.py
from fastapi import APIRouter, Depends
from core.dependencies import require_role
from schemas.user import UserOut

router = APIRouter(prefix="/admin", tags=["admin"])

@router.get("/dashboard", response_model=UserOut)
def get_admin_dashboard(current_user = Depends(require_role(["admin"]))):
    return current_user
```

## 📋 Bài tập
1. Cập nhật model User có trường role.
2. Gán role = "admin" nếu đăng ký bằng username là "admin", còn lại là "user".
3. Viết API /admin/dashboard chỉ cho admin truy cập.
4. Test bằng token "user" và "admin".