from fastapi import FastAPI, Form, File, UploadFile
from pydantic import BaseModel

app = FastAPI()

# 📌 1. Path Parameters
@app.get("/user/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}

# 📌 2. Query Parameters
@app.get("/items")
def list_items(page: int = 1, limit: int = 10):
    return {"page": page, "limit": limit}

# 📌 3. Body (JSON)
class Product(BaseModel):
    name: str
    price: float

@app.post("/products")
def create_product(product: Product):
    return {"name": product.name, "price": product.price}

# 📌 4. Form data
@app.post("/login")
def login(username: str = Form(...), password: str = Form(...)):
    return {"username": username, "message": "Login attempt"}

# 📌 5. Upload File
@app.post("/upload")
def upload(file: UploadFile = File(...)):
    return {
        "filename": file.filename,
        "content_type": file.content_type
    }
