class Student:
    def __init__(self, studentId, name, age):
        self.studentId = studentId
        self.name = name
        self.age = age

    def __str__(self):
        return f"[{self.studentId}] {self.name} - {self.age} years old"
    