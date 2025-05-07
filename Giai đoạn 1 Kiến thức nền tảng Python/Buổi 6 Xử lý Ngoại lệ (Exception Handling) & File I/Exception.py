'''
Cú pháp cơ bản
try:
    # khối lệnh có thể gây lỗi
except SomeException as e:
    # khối lệnh xử lý khi xảy ra SomeException
else:
    # khối lệnh chạy khi không có lỗi
finally:
    # khối lệnh luôn chạy, có lỗi hay không 
'''

# try: thử chạy khối lệnh
# except: bắt cụ thể 1 hoặc nhiều loại lỗi (có thể dùng chung except Exception)
# else: chạy khi khối try không có lỗi
# finally: luôn chạy cuối cùng (dùng để đóng tài nguyên, dọn dẹp)

def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError as e:
        print("Lỗi: Không thể chia cho 0.")
        return None
    except TypeError as e:
        print("Lỗi: Kiểu dữ liệu không hợp lệ.", e)
        return None
    else:
        print("Phép chia thành công, kết quả:", result)
        return result
    finally:
        print("Operation completed.")

# Thử nghiệm
safe_divide(10, 2)
safe_divide(10, 0)
safe_divide(10, "5")


# Ném ngoại lệ (raise)
#   Dùng khi muốn tự tạo và ném lỗi của riêng bạn:
def check_age(age):
    if age < 0:
        raise ValueError("Tuổi không thể là số âm.")
    print("Tuổi hợp lệ:", age)

# File I/O với Context Manager
# Đọc và ghi file
#   Mở file: open(filename, mode, encoding)
#       mode: 'r' (read), 'w' (write, ghi đè), 'a' (append), 'r+' (read/write)
#   Đóng file: luôn phải close() sau khi dùng, hoặc dùng with để Python tự đóng

# Context Manager (with open)
# Ghi file văn bản
with open('example.txt', 'w', encoding='utf-8') as f:
    f.write("Xin chào Python!\n")
    f.write("Buoi 6: File I/O va Exception Handling.\n")

# Đọc file toàn bộ nội dung
with open('example.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    print(content)

# Đọc từng dòng
with open('example.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print("Dòng:", line.strip())

# with đảm bảo file được đóng tự động ngay cả khi có lỗi xảy ra bên trong khối.
