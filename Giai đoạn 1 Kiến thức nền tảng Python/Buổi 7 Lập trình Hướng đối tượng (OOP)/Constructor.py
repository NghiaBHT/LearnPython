#2. Constructor: __init__ và Instance Attributes
#__init__ tự động được gọi khi tạo object, dùng để khởi tạo thuộc tính.
class Person:
    def __init__(self, name, age):
        self.name = name    # instance attribute
        self.age = age

# Khởi tạo và truy cập thuộc tính
p = Person("Nghĩa", 24)
print(p.name, p.age)     # Nghĩa 24

