from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas.order import Order, OrderIn
from app.services.order_service import list_orders, create_order

router = APIRouter(prefix="/orders", tags=["Orders"])

@router.get("/", response_model=List[Order])
def get_orders():
    return list_orders()

@router.post("/", response_model=Order, status_code=201)
def add_order(data: OrderIn):
    return create_order(data)
