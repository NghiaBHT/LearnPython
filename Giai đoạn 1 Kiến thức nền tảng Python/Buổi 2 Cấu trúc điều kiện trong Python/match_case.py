# Cú pháp cơ bản match-case
def handle_command(command):
    match command:
        case "start":
            print("Bắt đầu")
        case "stop":
            print("Dừng lại")
        case "pause":
            print("Tạm dừng")
        case _:
            print("Lệnh không hợp lệ")

handle_command("pause")   # → Tạm dừng

# So khớp nhiều giá trị (OR)
def handle_value(value):
    match value:
        case "yes" | "y":
            print("Bạn chọn Có")
        case "no" | "n":
            print("Bạn chọn Không")

handle_value("y")

# So khớp theo kiểu dữ liệu & cấu trúc (tuple, list...)
def handle_point(point):
    point = (0, 0)
    match point:
        case (0, 0):
            print("Gốc toạ độ")
        case (x, 0):
            print(f"Trên trục X, x={x}")
        case (0, y):
            print(f"Trên trục Y, y={y}")
        case (x, y):
            print(f"Điểm thường: x={x}, y={y}")

# So khớp dictionary (dict pattern matching)
def handle_pattern(pattern):
    person = {"name": "Nghĩa", "age": 24}
    match person:
        case {"name": name, "age": age}:
            print(f"Tên: {name}, Tuổi: {age}")
