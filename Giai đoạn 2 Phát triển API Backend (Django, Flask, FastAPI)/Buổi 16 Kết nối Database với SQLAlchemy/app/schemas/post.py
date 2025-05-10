from pydantic import BaseModel
from typing import Optional

class PostBase(BaseModel):
    title: str
    content: str

class PostCreate(PostBase):
    owner_id: int

class PostOut(PostBase):
    id: int
    owner_id: int

    class Config:
        from_attributes = True
