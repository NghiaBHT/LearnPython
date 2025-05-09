from pydantic import BaseModel, confloat, constr, validator
from typing import List

class ProductIn(BaseModel):
    name: constr(min_length=3, pattern=r'^[A-Za-z0-9 ]+$')
    price: confloat(gt=0)
    tags: List[constr(min_length=2)]

    @validator('tags', each_item=True)
    def tag_no_digit(cls, v):
        if any(c.isdigit() for c in v):
            raise ValueError('Tag không chứa chữ số')
        return v.lower()

class Product(ProductIn):
    id: int

    class Config:
        orm_mode = True


