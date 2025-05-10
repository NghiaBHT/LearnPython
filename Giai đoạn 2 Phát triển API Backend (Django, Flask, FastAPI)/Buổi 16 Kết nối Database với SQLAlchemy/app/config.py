import os

class Settings:
    # Ví dụ: postgresql://user:password@localhost:5432/mydb
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql://postgres:20122001@localhost:5432/mydb")

settings = Settings()

