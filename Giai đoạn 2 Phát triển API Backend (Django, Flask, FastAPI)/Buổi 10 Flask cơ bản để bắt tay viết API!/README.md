# 1. Giới thiệu về Flask
Flask là một web framework nhẹ và linh hoạt cho Python, lý tưởng cho việc phát triển RESTful API nhỏ và vừa.
So với Django, Flask ít "bắt buộc", giúp bạn tự do hơn trong cách tổ chức code.
# 2. Cài đặt Flask
- Bước 1: Kích hoạt môi trường ảo
    ```
    # Đảm bảo bạn đang trong thư mục project
    source .venv/bin/activate  # hoặc .venv\Scripts\activate trên   Windows
    ```
- Bước 2: Cài Flask
    ```
    pip install flask
    pip freeze > requirements.txt
    ```
# 3. Tạo API đơn giản với Flask
Chạy Flask app
```
python src/app.py
```