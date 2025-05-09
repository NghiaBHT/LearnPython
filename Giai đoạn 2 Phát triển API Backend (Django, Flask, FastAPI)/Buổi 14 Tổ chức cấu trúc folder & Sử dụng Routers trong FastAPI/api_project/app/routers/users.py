from fastapi import APIRouter
from typing import Dict

router = APIRouter()

@router.get("/{username}")
def user_name(username: str):
    return {
        "username": username,
        "message": "User detail here"
    }
