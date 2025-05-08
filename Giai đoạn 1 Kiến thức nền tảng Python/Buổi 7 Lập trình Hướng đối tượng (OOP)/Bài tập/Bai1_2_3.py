# Bài 1
class Person: 
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        print(f"Xin chào, tôi là {self.name}, {self.age} tuổi. ")
#Bài 2
class Student(Person):
    def __init__(self, name, age, major):
         super().__init__(name, age)
         self.major = major

    def introduce(self):
        super().introduce()
        print(f"Tôi học ngành {self.major}. ")
#Bai 3
class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def introduce(self):
        super().introduce() 
        print(f"Tôi dạy môn {self.subject}.")
        

# Thử nghiệm
s = Student("Nghĩa", 24, "Software Engineering")
t = Teacher("Anh", 35, "Toán")
s.introduce()
# Xin chào, tôi là Nghĩa, 24 tuổi.
# Tôi học ngành Software Engineering.
t.introduce()
# Xin chào, tôi là Anh, 35 tuổi.
# Tôi dạy môn Toán.