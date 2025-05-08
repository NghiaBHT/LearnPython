#4. Class Attributes & Static/ Class Methods
# Class attributes: chung cho tất cả instance.
# @classmethod: nhận cls (class) thay vì self.
# @staticmethod: không nhận self hay cls.

class Student:
    school = "FPT University"   # class attribute

    def __init__(self, name):
        self.name = name

    @classmethod
    def get_school(cls):
        return cls.school

    @staticmethod
    def info():
        return "Sinh viên ngành Software Engineering"

print(Student.get_school())  # FPT University
print(Student.info())       # Sinh viên ngành Software Engineering
