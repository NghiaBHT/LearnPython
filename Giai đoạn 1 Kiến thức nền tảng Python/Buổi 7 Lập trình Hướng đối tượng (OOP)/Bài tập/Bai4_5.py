# Bài 4 & 5
class Course:
    school_name = "FPT University"

    def __init__(self, course_name):
        self.course_name = course_name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def get_student_count(self):
        return len(self.students)

    def __len__(self):
        return len(self.students)

    def __str__(self):
        return f"{self.course_name} ({self.get_student_count()} sinh viên) - {Course.school_name}"

# Thử nghiệm Course
course = Course("Python OOP Mastery")
course.add_student(["Nghĩa", 24, "Software Engineering"])
course.add_student(["Lan", 22, "IT"])
print(course.get_student_count())
print(len(course))      # 2
print(course)           # Python OOP Mastery (2 sinh viên) - FPT University
