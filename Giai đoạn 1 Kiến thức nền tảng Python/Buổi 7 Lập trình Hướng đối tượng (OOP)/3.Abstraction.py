from abc import ABC, abstractmethod #Abstract Base Class
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("Gau Gau")
    
class Cat(Animal):
    def make_sound(self):
        print("Meo Meo")

dog = Dog()
cat = Cat()

dog.make_sound()
cat.make_sound()