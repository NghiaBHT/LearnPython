#Dùng để lặp qua danh sách, chuỗi, hoặc dãy số.
#for biến in dãy:
    # khối lệnh lặp

# Lặp qua các phần tử trong list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Lặp qua các ký tự trong chuỗi
for char in "Python":
    print(char)

# Lặp qua dãy số với range()
for i in range(5):  # i sẽ từ 0 đến 4
    print(i)

#3. break và continue
# - break: Dùng để thoát khỏi vòng lặp ngay lập tức.
# - continue: Dùng để bỏ qua phần còn lại của vòng lặp và tiếp tục với lần lặp tiếp theo.
 
# Dùng break
for i in range(10):
    if i == 5:
        break
    print(i)

# Dùng continue
for i in range(5):
    if i == 2:
        continue
    print(i)
