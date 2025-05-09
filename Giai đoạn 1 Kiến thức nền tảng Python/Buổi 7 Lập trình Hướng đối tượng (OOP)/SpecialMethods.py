# 7. Special Methods (Magic Methods)
# __str__ / __repr__: định nghĩa cách in object
# __add__, __len__,… cho phép overload toán tử
class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __add__(self, other):       # vector addition
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(4, 1)
v3 = v1 + v2
print(v3)  # Vector(6, 4)
