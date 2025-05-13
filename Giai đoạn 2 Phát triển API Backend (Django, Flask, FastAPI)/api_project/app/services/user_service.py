from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db import models
from app.db.database import SessionLocal
from app.schemas.user import UserCreate

async def get_user(db: Session, user_id: int):
    return await db.query(models.User).filter(models.User.id == user_id).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()
    
def create_user(db: Session, user: UserCreate):
    try:
        existing_user = db.query(models.User).filter(models.User.email == user.email or models.User.username == user.username).first()
        if existing_user:
            raise HTTPException(status_code=400, detail="User already registered")

        db_user = models.User(
            username=user.username,
            email=user.email    
        )

        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    except Exception as ex:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"{str(ex)}")

def delete_user(db: Session, user_id: int):
    u = get_user(db, user_id)
    if u:
        db.delete(u)
        db.commit()
    return u