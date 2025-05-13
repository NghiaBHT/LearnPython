from typing import List
from pydantic import BaseModel, EmailStr

class PostOut(BaseModel):
    id: int
    title: str
    content: str
    
    class Config:
        from_attributes = True

class UserBase(BaseModel):
    username: str
    email: EmailStr
    role: str

class UserCreate(UserBase):
    password: str

class UserOut(UserBase):
    id: int
    posts: List[PostOut] = []
    class Config:
        from_attributes = True