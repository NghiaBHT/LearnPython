from pydantic import BaseModel, EmailStr
from typing import List

class PostOut(BaseModel):
    id: int
    title: str
    content: str

    class Config:
        from_attributes = True

class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(UserBase):
    pass

class UserOut(UserBase):
    id: int
    posts: List[PostOut] = []

    class Config:
        from_attributes = True
