# 🎯 Buổi 12: Cài đặt FastAPI, chạy project đầu tiên
1. Tạo môi trường ảo và cài đặt FastAPI
```
python -m venv venv
venv\Scripts\activate
pip install fastapi uvicorn
```
📦 fastapi: framework chính
🚀 uvicorn: server ASGI chạy FastAPI

2. Chạy server
```
uvicorn main:app --reload
```
- main: tên file (main.py)
- app: tên ứng dụng FastAPI
- --reload: tự reload khi có thay đổi

Truy cập: http://localhost:8000
- 📌 Docs tự sinh: http://localhost:8000/docs
- 📌 Schema JSON: http://localhost:8000/openapi.json