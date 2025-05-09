from typing import List
from app.schemas.product import Product, ProductIn

_db: List[Product] = []
_next_id = 1

def list_products() -> List[Product]:
    return _db

def create_product(data: ProductIn) -> Product:
    global _next_id
    prod = Product(id=_next_id, **data.dict())
    _db.append(prod)
    _next_id += 1
    return prod
