# Khai báo và gọi hàm
# def tên_hàm(tham_số_1, tham_số_2, ...):
    # thân hàm
#   return giá_trị_trả_về

# Khai báo và gọi hàm
def greet(name):
    return f"Xin chào {name}!"

# Gọi hàm
print(greet("Nghĩa"))

# Hàm không có tham số và không trả giá trị
def say_hello():
    print("Hello world!")

say_hello()

# Hàm có tham số và có giá trị trả về (return)
def add(a, b):
    return a + b

result = add(3, 5)
print(result)

# Tham số mặc định
def greet(name="Bạn"):
    print(f"Xin chào {name}!")

greet()           # => Xin chào Bạn!
greet("Trọng")    # => Xin chào Trọng!

# Trả về nhiều giá trị
def get_name_and_age():
    return "Nghĩa", 23

name, age = get_name_and_age()
print(name)
print(age)

