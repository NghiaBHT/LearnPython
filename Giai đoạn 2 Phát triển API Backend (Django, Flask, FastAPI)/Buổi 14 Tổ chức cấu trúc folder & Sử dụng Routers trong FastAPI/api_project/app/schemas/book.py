from pydantic import BaseModel
from typing import Optional

class BookIn(BaseModel):
    title: str
    author: str

class BookOut(BookIn):
    id: int

    class Config:
        orm_mode = True
