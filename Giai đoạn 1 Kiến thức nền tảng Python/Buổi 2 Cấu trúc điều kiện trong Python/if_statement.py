# Câu lệnh if trong Python
# Câu lệnh if trong Python được sử dụng để kiểm tra một điều kiện và thực hiện một hành động nếu điều kiện đó đúng.
# Cú pháp của câu lệnh if trong Python như sau:
# if điều_kiện:
#     # thực hiện hành động nếu điều kiện đúng
# Ví dụ: Kiểm tra xem một số có phải là số dương hay không
number = 5
if number > 0:
    print("Số dương")
# Nếu điều kiện number > 0 đúng, chương trình sẽ in ra "Số dương".
'''----------------------------------------------------------------------------------------------------------------'''
# Câu lệnh if-else
# Nếu bạn muốn thực hiện một hành động khác nếu điều kiện không đúng, bạn có thể sử dụng câu lệnh else.
# Cú pháp của câu lệnh if-else trong Python như sau:
# if điều_kiện:
#     # thực hiện hành động nếu điều kiện đúng
# else:
#     # thực hiện hành động nếu điều kiện sai
# Ví dụ: Kiểm tra xem một số có phải là số dương hay không
number = -5
if number > 0:
    print("Số dương")
else:
    print("Số không dương")
# Nếu điều kiện number > 0 sai, chương trình sẽ in ra "Số không dương".
# Nếu điều kiện number > 0 đúng, chương trình sẽ in ra "Số dương".
'''----------------------------------------------------------------------------------------------------------------'''
# Câu lệnh if-elif-else
# Nếu bạn muốn kiểm tra nhiều điều kiện khác nhau, bạn có thể sử dụng câu lệnh if-elif-else.
# Cú pháp của câu lệnh if-elif-else trong Python như sau:
# if điều_kiện_1:
#     # thực hiện hành động nếu điều kiện 1 đúng
# elif điều_kiện_2:
#     # thực hiện hành động nếu điều kiện 2 đúng
# elif điều_kiện_3:
#     # thực hiện hành động nếu điều kiện 3 đúng
# else:
#     # thực hiện hành động nếu tất cả các điều kiện trên đều sai
# Ví dụ: Kiểm tra xem một số là số dương, số âm hay số không
number = 0
if number > 0:
    print("Số dương")
elif number < 0:
    print("Số âm")
else:
    print("Số không")
# Nếu điều kiện number > 0 đúng, chương trình sẽ in ra "Số dương".
# Nếu điều kiện number < 0 đúng, chương trình sẽ in ra "Số âm".
# Nếu cả hai điều kiện trên đều sai, chương trình sẽ in ra "Số không".
# Nếu điều kiện number > 0 sai, chương trình sẽ kiểm tra điều kiện number < 0.
# Nếu điều kiện number < 0 đúng, chương trình sẽ in ra "Số âm".
# Nếu cả hai điều kiện trên đều sai, chương trình sẽ in ra "Số không".
'''----------------------------------------------------------------------------------------------------------------'''
# Câu lệnh if lồng nhau
# Bạn có thể lồng câu lệnh if bên trong một câu lệnh if khác để kiểm tra nhiều điều kiện phức tạp hơn.
# Cú pháp của câu lệnh if lồng nhau trong Python như sau:
# if điều_kiện_1:
#     if điều_kiện_2:
#         # thực hiện hành động nếu điều kiện 1 và 2 đều đúng
#     else:
#         # thực hiện hành động nếu điều kiện 1 đúng và điều kiện 2 sai
# else:
#     # thực hiện hành động nếu điều kiện 1 sai
# Ví dụ: Kiểm tra xem một số có phải là số dương và chẵn hay không
number = 4
if number > 0:
    if number % 2 == 0:
        print("Số dương và chẵn")
    else:
        print("Số dương và lẻ")
# Nếu điều kiện number > 0 đúng và điều kiện number % 2 == 0 đúng, chương trình sẽ in ra "Số dương và chẵn".
# Nếu điều kiện number > 0 đúng và điều kiện number % 2 == 0 sai, chương trình sẽ in ra "Số dương và lẻ".
# Nếu điều kiện number > 0 sai, chương trình sẽ không thực hiện bất kỳ hành động nào.
# Nếu điều kiện number > 0 đúng, chương trình sẽ kiểm tra điều kiện number % 2 == 0.
# Nếu điều kiện number % 2 == 0 đúng, chương trình sẽ in ra "Số dương và chẵn".
# Nếu điều kiện number % 2 == 0 sai, chương trình sẽ in ra "Số dương và lẻ".
'''----------------------------------------------------------------------------------------------------------------'''
# Câu lệnh if với nhiều điều kiện
# Bạn có thể sử dụng toán tử logic để kết hợp nhiều điều kiện trong câu lệnh if.
# Các toán tử logic phổ biến trong Python bao gồm and, or và not.
# - and: Trả về True nếu cả hai điều kiện đều đúng.
# - or: Trả về True nếu ít nhất một trong hai điều kiện đúng.
# - not: Trả về True nếu điều kiện sai.
# Ví dụ: Kiểm tra xem một số có phải là số dương và chẵn hay không
