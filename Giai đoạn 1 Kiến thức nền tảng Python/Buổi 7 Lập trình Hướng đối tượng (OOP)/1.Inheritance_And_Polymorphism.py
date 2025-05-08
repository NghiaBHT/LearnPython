# 5. Kế thừa (Inheritance) & Đa hình (Polymorphism)
# Kế thừa: class con kế thừa thuộc tính và phương thức của class cha.
# Đa hình: class con có thể override (ghi đè) phương thức.

class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):           # override
        print("Dog barks")

class Cat(Animal):
    def speak(self):           # override
        print("Cat meows")

animals = [Dog(), Cat(), Animal()]
for a in animals:
    a.speak()

# Dog barks
# Cat meows
# Animal speaks
