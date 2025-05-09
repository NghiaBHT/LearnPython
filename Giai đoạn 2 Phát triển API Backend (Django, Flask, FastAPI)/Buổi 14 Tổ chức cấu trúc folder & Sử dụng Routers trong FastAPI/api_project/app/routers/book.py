from fastapi import APIRouter, HTTPException
from typing import List
from ..schemas.book import BookIn, BookOut
from ..services.book_service import list_books, create_book

router = APIRouter()

@router.get("/", response_model=List[BookOut])
def get_books():
    return list_books()

@router.post("/", response_model=BookOut, status_code=201)
def add_book(book: BookIn):
    return create_book(book)

