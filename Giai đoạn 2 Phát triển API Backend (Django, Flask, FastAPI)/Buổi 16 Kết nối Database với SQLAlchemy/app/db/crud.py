from sqlalchemy.orm import Session
from app.db import models
from app.schemas.user import UserCreate
from app.schemas.post import PostCreate
from typing import List, Dict

# ----- User CRUD -----
def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: UserCreate):
    db_user = models.User(username=user.username, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    u = get_user(db, user_id)
    if u:
        db.delete(u)
        db.commit()
    return u

# ----- Post CRUD -----
def get_post(db: Session, post_id: int):
    return db.query(models.Post).filter(models.Post.id == post_id).first()

def get_posts_by_user(db: Session, user_id: int):
    return db.query(models.Post).filter(models.Post.owner_id == user_id).all()

def create_post(db: Session, post: PostCreate):
    db_post = models.Post(**post.dict())
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

def delete_post(db: Session, post_id: int):
    p = get_post(db, post_id)
    if p:
        db.delete(p)
        db.commit()
    return p
