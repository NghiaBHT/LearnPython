from fastapi import FastAPI
from .routers import health, book, users
def create_app() -> FastAPI:
    app =  FastAPI(title= "My Fast Api Project")

    # Mount routers
    app.include_router(health.router, prefix="/health", tags=["Health"])
    app.include_router(book.router, prefix="/books", tags=["Books"])
    app.include_router(users.router, prefix="/users", tags=["Users"])
    return app

app = create_app()