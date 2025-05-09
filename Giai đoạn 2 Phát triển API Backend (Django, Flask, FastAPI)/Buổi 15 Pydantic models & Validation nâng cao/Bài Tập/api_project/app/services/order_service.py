from typing import List
from app.schemas.order import Order, OrderIn

_db: List[Order] = []
_next_id = 1

def list_orders() -> List[Order]:
    return _db

def create_order(data: OrderIn) -> Order:
    global _next_id
    order = Order(id = _next_id, total = 0, **data.dict())
    _db.append(order)
    _next_id += 1
    return order

