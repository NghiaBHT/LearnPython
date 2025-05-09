from typing import List
from ..schemas.book import BookIn, BookOut

# Đây là ví dụ tạm, dùng list in-memory
_db: List[BookOut] = []

def list_books() -> List[BookOut]:
    return _db

def create_book(data: BookIn) -> BookOut:
    new = BookOut(id=len(_db)+1, **data.dict())
    _db.append(new)
    return new
