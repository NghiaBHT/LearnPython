# 6. Đóng gói (Encapsulation)
# Python không có private thật, nhưng quy ước:
# _attr: protected (không nên truy cập trực tiếp ngoài class/subclass)
# __attr: name mangling (tránh đụng tên)
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   # “private”

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance

acct = BankAccount(1000)
acct.deposit(500)
print(acct.get_balance())       # 1500
# print(acct.__balance)        # AttributeError
