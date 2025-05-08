Bài tập Buổi 7
1. Class Person
    Thuộc tính: name, age
    Phương thức introduce(): in “Xin chào, tôi là {name}, {age} tuổi.”
    
2. Class Student (thừa kế Person)
    Thêm thuộc tính major (chuyên ngành)
    Override introduce() để in thêm “Tôi học ngành {major}.”

3. Class Teacher (thừa kế Person)
    Thêm thuộc tính subject (môn dạy)
    Override introduce() để in thêm “Tôi dạy môn {subject}.”

4. Class Course
    Class attribute: school_name = "FPT University"
    Instance attributes: course_name, students (list rỗng)
    Methods:
        add_student(student: Student)
        get_student_count()

5. Sử dụng special methods
    Trong Course, implement __len__() để len(course) trả về số học sinh.
    Implement __str__() để in gọn thông tin khoá học.