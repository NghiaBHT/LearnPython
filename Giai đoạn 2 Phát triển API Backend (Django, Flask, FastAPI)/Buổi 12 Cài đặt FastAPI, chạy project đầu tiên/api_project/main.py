from fastapi import FastAPI
from pydantic import BaseModel

class sumInput(BaseModel):
    a: int
    b: int


app = FastAPI()

@app.get("/")
def read_root():
    return {"meggage": "Hello world Fast API"}

@app.get("/hello")
def hello(name: str):
    return {"message": f"Hello {name}"}

@app.get("/square/{number}")
def square(number: int):
    return {"message": f"number: {number ** 2}"}

@app.post("/sum")    
def sum(data: sumInput):
    return {"message": data.a + data.b}

