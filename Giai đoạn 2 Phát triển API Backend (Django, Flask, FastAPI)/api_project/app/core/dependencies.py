from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db import models
from app.core.security import verify_token  # Giả sử verify_token là hàm bạn dùng để giải mã token
from app.db.database import SessionLocal  # Hàm lấy session của DB
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally:
        db.close

security = HTTPBearer()

def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)
):
    username = verify_token(credentials.credentials)
    if not username:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    
    user = db.query(models.User).filter(models.User.username == username).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    return user

def require_role(required_roles: list[str]):
    def role_checker(current_user: models.User = Depends(get_current_user)):
        if current_user.role not in required_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Permission denied"
            )
        return current_user
    return role_checker