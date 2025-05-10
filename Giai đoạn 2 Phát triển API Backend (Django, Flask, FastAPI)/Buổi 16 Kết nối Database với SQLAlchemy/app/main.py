from fastapi import FastAPI
from app.db.database import Base, engine
from app.routers import users, posts

# Tạo bảng nếu chưa có
Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI + PostgreSQL + Alembic Example")

app.include_router(users.router)
app.include_router(posts.router)
