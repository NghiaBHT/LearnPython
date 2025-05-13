import os


class Settings:
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql://postgres:20122001@localhost:5432/mydb")

settings = Settings()