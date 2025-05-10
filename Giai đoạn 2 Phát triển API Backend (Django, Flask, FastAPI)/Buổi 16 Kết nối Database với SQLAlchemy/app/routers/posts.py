from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import crud
from app.db.database import SessionLocal
from app.schemas.post import PostCreate, PostOut
from typing import List

router = APIRouter(prefix="/posts", tags=["posts"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=PostOut)
def create_post(post: PostCreate, db: Session = Depends(get_db)):
    # Kiểm tra user tồn tại
    from app.db.crud import get_user
    if not get_user(db, post.owner_id):
        raise HTTPException(404, "Owner not found")
    return crud.create_post(db, post)

@router.get("/", response_model=List[PostOut])
def list_posts(db: Session = Depends(get_db)):
    # Lấy tất cả post
    return db.query(crud.models.Post).all()

@router.get("/user/{user_id}", response_model=List[PostOut])
def posts_by_user(user_id: int, db: Session = Depends(get_db)):
    return crud.get_posts_by_user(db, user_id)

@router.get("/{post_id}", response_model=PostOut)
def read_post(post_id: int, db: Session = Depends(get_db)):
    p = crud.get_post(db, post_id)
    if not p:
        raise HTTPException(404, "Post not found")
    return p

@router.delete("/{post_id}", response_model=PostOut)
def delete_post(post_id: int, db: Session = Depends(get_db)):
    p = crud.delete_post(db, post_id)
    if not p:
        raise HTTPException(404, "Post not found")
    return p
