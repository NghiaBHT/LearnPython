# Bài 1: List
nums = [3, 1, 4, 1, 5, 9, 2]
nums.append(6)           # [3,1,4,1,5,9,2,6]
nums.insert(2, 7)        # [3,1,7,4,1,5,9,2,6]
nums.remove(1)           # chỉ xóa 1 phần tử 1 đầu tiên
nums.sort()              # [1,2,3,4,5,6,7,9]
print(nums)

# Bài 2: Tuple
def swap(a, b):
    return (b, a)

print(swap(10, 20))      # (20, 10)

# Bài 3: Set
unique = set(nums)
print("Set từ nums:", unique)     # ví dụ {1,2,3,4,5,6,7,9}

A = {1,2,3}
B = {3,4,5}
print("A ∪ B =", A.union(B))
print("A ∩ B =", A.intersection(B))
print("A – B =", A.difference(B))

# Bài 4: Dictionary
keys = ["name", "age", "city"]
vals = ["Anh", 30, "Hanoi"]
d = dict(zip(keys, vals))
d["age"] = 31
d.pop("city")
for k, v in d.items():
    print(k, ":", v)
