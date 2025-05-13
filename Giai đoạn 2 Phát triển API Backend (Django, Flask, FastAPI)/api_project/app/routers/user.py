from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.dependencies import get_current_user, require_role
from app.db.database import SessionLocal
from app.schemas.user import UserCreate, UserOut
from app.services import user_service


router = APIRouter(prefix="/users", tags=["users"])

def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally:
        db.close


@router.post("/", response_model=UserOut)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return user_service.create_user(db, user)

@router.get("/", response_model=List[UserOut])
def list_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return user_service.get_users(db, skip, limit)

@router.get("/me", response_model=UserOut)
def get_me(current_user = Depends(get_current_user)):
    return current_user

@router.get("/dashboard", response_model=UserOut)
def get_admin_dashboard(current_user = Depends(require_role(["admin"]))):
    return current_user