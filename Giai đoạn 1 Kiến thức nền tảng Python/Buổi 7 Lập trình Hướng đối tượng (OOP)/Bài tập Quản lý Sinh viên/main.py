from StudentManager import StudentManager  # ⚠️ Import đúng tên file

def main():
    manager = StudentManager()

    while True:
        print("\n--- Menu ---")
        print("1. Thêm sinh viên")
        print("2. Hiển thị danh sách sinh viên")
        print("3. Cập nhật sinh viên")
        print("4. Xoá sinh viên")
        print("5. Thoát")

        choice = input("Chọn chức năng: ")

        if choice == '1':
            sid = input("Nhập ID: ")
            name = input("Nhập tên: ")
            age = int(input("Nhập tuổi: "))
            manager.create_student(sid, name, age)
        elif choice == '2':
            manager.read_students()
        elif choice == '3':
            sid = input("Nhập ID sinh viên cần cập nhật: ")
            name = input("Tên mới: ")
            age = int(input("Tuổi mới: "))
            manager.update_student(sid, name, age)
        elif choice == '4':
            sid = input("Nhập ID sinh viên cần xoá: ")
            manager.delete_student(sid)
        elif choice == '5':
            print("👋 Thoát chương trình.")
            break
        else:
            print("❌ Lựa chọn không hợp lệ.")

if __name__ == "__main__":
    main()
