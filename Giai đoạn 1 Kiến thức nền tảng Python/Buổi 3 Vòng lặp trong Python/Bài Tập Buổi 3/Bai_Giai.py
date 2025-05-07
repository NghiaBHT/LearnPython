# Bài 1: In 1 đến 10
for i in range(1, 11):
    print(i, end=" ")
    # # Kết quả sẽ là:
    # # 1 2 3 4 5 6 7 8 9 10

# Bài 2: In số chẵn từ 2 đến 20
for i in range(2, 21, 2):
    print(i, end=" ")
    # # Kết quả sẽ là:
    # # 2 4 6 8 10 12 14 16 18 20

# Bài 3: Tổng từ 1 đến n
for i in range(1, 11):
    total = 0
    total += i
    print("Tổng từ 1 đến", i, "là:", total)

# Bài 4: Bảng cửu chương của 5
for i in range(1, 10):
    print("5 x ",i," = ", 5*i)

# Bài 5: Đếm ký tự chữ cái
string = "Hello World!"
count = 0
for char in string:
    if char.isalpha():
        count += 1
print("Số ký tự chữ cái trong chuỗi là:", count)