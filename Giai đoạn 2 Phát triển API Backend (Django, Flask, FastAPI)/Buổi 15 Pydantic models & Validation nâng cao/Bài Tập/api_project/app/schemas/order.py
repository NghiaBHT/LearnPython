from pydantic import BaseModel, constr, validator
from typing import List
from .product import Product

class OrderIn(BaseModel):
    user_id: int
    products: List[Product]
    status: constr(pattern=r'^(pending|shipped|delivered)$')

class Order(OrderIn):
    id: int
    total: float

    @validator('total', pre=True, always=True)
    def calc_total(cls, v, values):
        prods = values.get('products', [])
        return sum(p.price for p in prods)

    class Config:
        orm_mode = True
