## 1. Khởi tạo project trên VSCode
- Bước 1: Tạo thư mục project
    1. Mở terminal (Ctrl+` trong VSCode).
    2. Chạy: 
        ```
        mkdir api_project
        cd api_project
        ```
- Bước 2: Tạo và kích hoạt môi trường ảo
    ```
    # Windows
    python -m venv .venv
    .venv\Scripts\activate

    # macOS/Linux
    python3 -m venv .venv
    source .venv/bin/activate
    ```
    | Khi active, bạn sẽ thấy (.venv) ở đầu dòng.
- Bước 3: Tạo file requirements.txt
    ```
    echo "# dependencies" > requirements.txt
    ```
    Chúng ta sẽ thêm các thư viện sau (khi đến buổi framework sẽ cài tiếp):
    - requests (client HTTP)
    - httpie (CLI testing)
    ```
    pip install requests httpie
    pip freeze > requirements.txt
    ```
- Bước 4: Mở thư mục trong VSCode
    - VSCode → File > Open Folder... → chọn api_project.
    - Cài extension nếu chưa có:
        - Python (Microsoft)
        - REST Client (làm file .http)
        - EditorConfig (nếu thích)
- Bước 5: Chọn Python Interpreter
    - Ctrl+Shift+P → “Python: Select Interpreter” → chọn ./.venv.

# 2. Cấu trúc thư mục gợi ý
```
    api_project/
    ├── .vscode/
    │   └── settings.json        # (tùy chọn) config riêng cho workspace
    ├── .venv/                   # môi trường ảo
    ├── src/
    │   └── http_examples.py     # code mẫu sử dụng requests/httpie
    ├── tests/
    │   └── test_http.py         # (sau này) để viết test
    ├── requests/
    │   └── books.http           # (REST Client) kịch bản GET/POST
    ├── requirements.txt
    └── README.md
```

- .vscode/settings.json (ví dụ):
```
    {
      "python.pythonPath": ".venv/bin/python",
      "python.formatting.provider": "black",
      "editor.formatOnSave": true
    }
```

- src/http_examples.py: đặt các ví dụ minh họa gọi HTTP.
- requests/books.http: dùng REST Client để lưu các request GET/POST.

