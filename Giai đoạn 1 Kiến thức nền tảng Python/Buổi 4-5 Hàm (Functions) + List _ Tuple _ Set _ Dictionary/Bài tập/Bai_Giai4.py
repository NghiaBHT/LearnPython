# Bài 1: Hàm tính tổng 2 số
def add(a, b):
    return a + b

print(add(3, 5))


# Bài 2: Hàm kiểm tra số chẵn
def is_even(n):
    return n % 2 == 0

print(is_even(4))  # True
print(is_even(5))  # False


# Bài 3: Hàm tìm số lớn nhất trong 3 số
def find_max(a, b, c):
    return max(a, b, c)

print(find_max(10, 20, 15))


# Bài 4: Hàm tính giai thừa
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

print(factorial(5))  # 120


# Bài 5: Hàm kiểm tra Palindrome
def is_palindrome(s):
    s = s.lower()  # bỏ qua phân biệt chữ hoa/thường
    return s == s[::-1]

print(is_palindrome("Madam"))  # True
print(is_palindrome("Hello"))  # False
