from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas.product import Product, ProductIn
from app.services.product_service import list_products, create_product

router = APIRouter(prefix="/products", tags=["Products"])

@router.get("/", response_model=List[Product])
def get_products():
    return list_products()

@router.post("/", response_model=Product, status_code=201)
def add_product(data: ProductIn):
    return create_product(data)
