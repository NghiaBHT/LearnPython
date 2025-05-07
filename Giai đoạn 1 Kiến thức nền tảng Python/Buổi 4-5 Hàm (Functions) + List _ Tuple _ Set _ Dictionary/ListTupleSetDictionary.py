# 1. List
# Định nghĩa: danh sách có thứ tự, cho phép nhiều lần lặp, thay đổi được (mutable).
# Tạo list:
lst = [1, 2, 3]
empty = []
# Truy cập & Slicing:
lst[0]       # 1  
lst[-1]      # 3  
lst[1:3]     # [2, 3]  
# Thao tác:
lst.append(4)        # thêm cuối  
lst.insert(1, 9)     # chèn tại index=1  
lst.pop()            # xoá và trả về phần tử cuối  
lst.remove(2)        # xoá phần tử có giá trị 2  
lst.sort()           # sắp xếp tăng dần  
lst.reverse()        # đảo ngược thứ tự  
len(lst)             # độ dài list  

# 2. Tuple
# Định nghĩa: bộ có thứ tự, cho phép lặp, không thay đổi được (immutable).
# Tạo tuple:
tup = (1, 2, 3)
single = (5,)        # dấu phẩy thể hiện tuple một phần tử  
# Truy cập & Slicing: tương tự list.
# Ứng dụng: lưu trữ cố định (tọa độ, cấu hình không đổi), trả về nhiều giá trị từ hàm.

# 3. Set
# Định nghĩa: tập hợp không thứ tự, không cho phép trùng lặp, mutable.
# Tạo set:
st = {1, 2, 3}
empty = set()        # chú ý: {} là dict, phải dùng set()

# Thao tác tập hợp:
st.add(4)              # thêm phần tử  
st.remove(2)           # xoá phần tử; KeyError nếu không tồn tại  
st.discard(5)          # xoá nếu có, không lỗi nếu không  
st.union({3,5})        # hợp  
st.intersection({2,3}) # giao  
st.difference({1,2})   # hiệu  
# Ứng dụng: loại bỏ phần tử trùng lặp, các phép toán tập hợp.

# 4. Dictionary
# Định nghĩa: cấu trúc key → value, không thứ tự (trên Python 3.7+ giữ thứ tự chèn), mutable.
# Tạo dict:
d = {"a": 1, "b": 2}
empty = {}

# Truy cập & Cập nhật:
d["a"]             # 1
d["c"] = 3         # thêm hoặc cập nhật
val = d.get("z", 0)# trả về 0 nếu key không tồn tại

# Xóa phần tử:
d.pop("b")         # xoá và trả về value
d.popitem()        # xoá cặp key-value cuối cùng

# Duyệt dict:
for k in d:       # key
    print(k, d[k])
for k, v in d.items():
    print(k, v)

# Các phương thức: keys(), values(), items(), update().

