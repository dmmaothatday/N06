from ManageStudents import ManageStudents
from Student import StudentA, StudentB

data = ManageStudents()
data.add_student(StudentA('1','S1','a','hn',10,10,10))
data.add_student(StudentB('2','S2','b','hn',1,2,3))
data.add_student(StudentA('3','S3','c','hn',1,1,1))
data.add_student(StudentB('4','S4','d','hn',2,2,2))
data.add_student(StudentA('5','S5','f','hn',3,4,5))
data.add_student(StudentA('6','S6','a','hn',10,10,10))
data.add_student(StudentA('7','S7','a','hn',10,10,10))
data.add_student(StudentA('8','S8','a','hn',10,10,10))
data.add_student(StudentA('9','S9','a','hn',10,10,10))
data.add_student(StudentA('10','S10','a','hn',10,10,10))
data.add_student(StudentA('11','S11','a','hn',10,10,10))

if __name__ == "__main__":
    while True:
        print('1. Thêm mới thí sinh')
        print('2. Tìm kiếm thí sinh')
        print('3. Sửa thông tin thí sinh')
        print('4. Xóa thí sinh')
        print('5. Hiển thị danh sách thí sinh có điểm để xét vào đại học')
        print('6. Hiển thị danh sách thí sinh đạt học bổng')
        print('7. Hiển thị danh sách thí sinh không liệt môn nào')
        print('8. Thoát chương trình')
        option = input('Vui lòng chọn chức năng (1-8): ')
        print()

        if option == '1': #Thêm mới thí sinh
            id_number = input('Nhập số CMND: ')
            candidate_number = input('Nhập số báo danh: ')
            name = input('Nhập họ và tên: ')
            address = input('Nhập địa chỉ: ')
            student_type = input('Loại thí sinh (A hoặc B): ')
            if student_type == 'A':
                math = float(input('Nhập điểm toán: '))
                physics = float(input('Nhập điểm lý: '))
                chemistry = float(input('Nhập điểm hóa: '))
                student = StudentA(id_number, candidate_number, name, address, math, physics, chemistry)
            elif student_type == 'B':
                math = float(input('Nhập điểm toán: '))
                chemistry = float(input('Nhập điểm hóa: '))
                biology = float(input('Nhập điểm sinh: '))
                student = StudentB(id_number, candidate_number, name, address, math, chemistry, biology)
            else:
                print('Loại thí sinh không hợp lệ')

            data.add_student(student)

            print('Thêm thí sinh thành công')
            print()
            pass

        elif option == '2':#Tìm kiếm thí sinh
            input_candidate_number = input("Nhập số báo danh của thí sinh cần tìm: ")
            found_student = data.find_student(candidate_number=input_candidate_number)
            if found_student is not None:
                print("Thông tin của thí sinh:")
                print("Số CMND:", found_student.id_number)
                print("Số báo danh:", found_student.candidate_number)
                print("Tên:", found_student.name)
                print("Địa chỉ:", found_student.address)
                if isinstance(found_student, StudentA):
                    print("Điểm Toán:", found_student.math)
                    print("Điểm Vật lý:", found_student.physics)
                    print("Điểm Hóa học:", found_student.chemistry)
                elif isinstance(found_student, StudentB):
                    print("Điểm Toán:", found_student.math)
                    print("Điểm Hóa học:", found_student.chemistry)
                    print("Điểm Sinh học:", found_student.biology)
            else:
                print("Số báo danh không tồn tại.")
                input_id = input("Vui lòng nhập số báo danh của thí sinh để tìm kiếm: ")
                found_by_id = data.find_student(id_number=input_id)
                if found_by_id is not None:
                    print("Thông tin của thí sinh:")
                    print("Số CMND:", found_by_id.id_number)
                    print("Số báo danh:", found_by_id.candidate_number)  # Lưu ý sửa đổi đến chữ hoa/thường ở đây
                    print("Tên:", found_by_id.name)
                    print("Địa chỉ:", found_by_id.address)
                    if isinstance(found_by_id, StudentA):
                        print("Điểm Toán:", found_by_id.math)
                        print("Điểm Vật lý:", found_by_id.physics)
                        print("Điểm Hóa học:", found_by_id.chemistry)
                    elif isinstance(found_by_id, StudentB):
                        print("Điểm Toán:", found_by_id.math)
                        print("Điểm Hóa học:", found_by_id.chemistry)
                        print("Điểm Sinh học:", found_by_id.biology)
                else:
                    print("Không tìm thấy thí sinh.")
                print()
            pass

        elif option == '3':#Sửa thông tin thí sinh
            candidate_number = input("Nhập số báo danh của thí sinh: ")
            id_number = input("Nhập số CMND thí sinh: ")

            new_info = {}
            new_info['name'] = input("Nhập tên mới của thí sinh (nhấn Enter nếu không thay đổi): ")
            new_info['address'] = input("Nhập địa chỉ mới của thí sinh (nhấn Enter nếu không thay đổi): ")
            exam_type = input("Nhập khối (A hoặc B): ")
            if exam_type == "A":
                new_info['math'] = float(input("Nhập điểm toán mới của thí sinh (nhấn Enter nếu không thay đổi): ") or found_student.math)
                new_info['physics'] = float(input("Nhập điểm vật lý mới của thí sinh (nhấn Enter nếu không thay đổi): ") or found_student.physics)
                new_info['chemistry'] = float(input("Nhập điểm hóa học mới của thí sinh (nhấn Enter nếu không thay đổi): ") or found_student.chemistry)
            elif exam_type == "B":
                new_info['math'] = float(input("Nhập điểm toán mới của thí sinh (nhấn Enter nếu không thay đổi): ") or found_student.math)
                new_info['chemistry'] = float(input("Nhập điểm hóa học mới của thí sinh (nhấn Enter nếu không thay đổi): ") or found_student.chemistry)
                new_info['biology'] = float(input("Nhập điểm toán mới của thí sinh (nhấn Enter nếu không thay đổi): ") or found_student.biology)
            else:
                print("Không tìm thấy thí sinh .")
            data.update_student(candidate_number, id_number, new_info)
            print("Sửa thông tin thành công")
            print()

            pass

        elif option == '4':#Xóa thí sinh
            input_candidate_number = input("Nhập số báo danh của thí sinh cần xóa: ")
            found_student = data.find_student(candidate_number=input_candidate_number)
            if found_student is not None:
                data.delete_student(input_candidate_number)
                print("Đã xóa thông tin của thí sinh có số báo danh:", input_candidate_number)
            else:
                print("Số báo danh không tồn tại.")
            
            print()
            pass

        elif option == '5':# Hiển thị danh sách thí sinh có điểm để xét vào đại học
            order = input("Nhập 'asc' để sắp xếp thứ tự từ thấp đến cao, hoặc 'desc' để sắp xếp từ cao đến thấp: ")
            sorted_students = data.sort_student_list_by_total_score(order)
            for student in sorted_students:
                print(f"id_number: {student.id_number}, name: {student.name}, score: {data.calculate_score(student)}")
            print()
            pass

        elif option == '6':# Hiển thị danh sách thí sinh đạt học bổng
            students_with_scholarship = data.get_students_with_scholarship()
            if students_with_scholarship is not None:
                for student in students_with_scholarship:
                    if isinstance(student, StudentA): #and data.calculate_score(student) >=32:
                        print(f"Tên: {student.name},  Điểm vào đại học: {data.calculate_score(student)}")
                    elif isinstance(student, StudentB): #and data.calculate_score(student) >=32:
                        print(f"Tên: {student.name},  Điểm vào đại học: {data.calculate_score(student)}")
            else:
                print("Không có thí sinh nào đạt học bổng.")
            print()
            pass

        elif option == '7':# Hiển thị danh sách thí sinh không liệt môn nào
            students_without_failed_subjects = data.get_student_list_without_failed_subjects()
            if students_without_failed_subjects is not None:
                for student in students_without_failed_subjects:
                    if isinstance(student, StudentA):
                        print(f"Tên: {student.name}, Toán: {student.math}, Lý: {student.physics}, Hóa: {student.chemistry}")
                    elif isinstance(student, StudentB):
                        print(f"Tên: {student.name}, Toán: {student.math}, Hóa: {student.chemistry}, Sinh: {student.biology}")
            else:
                print("không có thí sinh trượt.")
            pass
        elif option == '8':
            print('Thoát chương trình')
            break
        else:
            print('Lựa chọn không hợp lệ, vui lòng chọn lại')