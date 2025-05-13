from pydantic import BaseModel


class PostBase(BaseModel):
    title: str
    content: str

class PostCreate(PostBase):
    user_id: int

class PostOut(PostBase):
    id: int
    user_id = int

    class Config:
        from_attributes = True

