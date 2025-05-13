from fastapi import FastAPI
from app.db.database import Base, engine
from app.routers import auth, user

def create_app() -> FastAPI:
    Base.metadata.create_all(bind=engine)
    app = FastAPI(title="User Manegerment")
    app.include_router(user.router)
    app.include_router(auth.router)
    return app

app = create_app()