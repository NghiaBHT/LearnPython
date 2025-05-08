from Student import Student  # ⚠️ Import đúng tên class (chữ hoa đầu)

class StudentManager:
    def __init__(self):
        self.students = []

    def create_student(self, student_id, name, age):
        self.students.append(Student(student_id, name, age))
        print("✅ Thêm sinh viên thành công.")

    def read_students(self):
        if not self.students:
            print("📭 Không có sinh viên nào.")
        else:
            for student in self.students:
                print(student)

    def update_student(self, student_id, new_name, new_age):
        for student in self.students:
            if student.student_id == student_id:
                student.name = new_name
                student.age = new_age
                print("✅ Cập nhật thành công.")
                return
        print("❌ Không tìm thấy sinh viên.")

    def delete_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                print("🗑️ Xoá thành công.")
                return
        print("❌ Không tìm thấy sinh viên.")
