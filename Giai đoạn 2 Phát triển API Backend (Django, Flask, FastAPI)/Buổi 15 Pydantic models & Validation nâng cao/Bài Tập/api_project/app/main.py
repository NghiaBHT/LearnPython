from fastapi import FastAPI
from app.routers import products, orders
def create_app() -> FastAPI:
    app = FastAPI(title="FastAPI Shop Example")

    # Mount routers
    app.include_router(products.router)
    app.include_router(orders.router)

    return app

app = create_app()
