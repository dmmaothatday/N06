from ManageStudents import ManageStudents
from Student import StudentA, StudentB

data = ManageStudents()
data.add_student(StudentA('1','S1','a','hn',10,10,10))
data.add_student(StudentB('2','S2','b','hn',1,2,3))
data.add_student(StudentA('3','S3','c','hn',1,1,1))
# data.add_student(StudentB('4','S4','d','hn',2,2,2))
# data.add_student(StudentA('5','S5','f','hn',3,4,5))
# data.add_student(StudentA('6','S6','a','hn',10,10,10))
# data.add_student(StudentA('7','S7','a','hn',10,10,10))
# data.add_student(StudentA('8','S8','a','hn',10,10,10))
# data.add_student(StudentA('9','S9','a','hn',10,10,10))
# data.add_student(StudentA('10','S10','a','hn',10,10,10))
# data.add_student(StudentA('11','S11','a','hn',10,10,10))

def is_valid_id_number(iid_number):
    # Kiểm tra xem số căn cước có đúng định dạng hay không
    # Đảm bảo id_number không chứa ký tự đặc biệt, không có khoảng trắng, là số nguyên dương và không trùng với id_number khác
    if not iid_number:
        print("Lỗi: Số CCCD không được để trống")
        return False  # Trả về False nếu tên rỗng
    if not iid_number.isdigit():
        print("Lỗi: Số căn cước chỉ được chứa chữ số")
        return False  # Trả về False nếu không phải toàn chữ số
    if ' ' in iid_number:
        print("Lỗi: Số căn cước không được chứa khoảng trắng")
        return False  # Trả về False nếu có khoảng trắng
    if int(iid_number) <= 0:
        print("Lỗi: Số căn cước phải là số nguyên dương")
        return False  # Trả về False nếu không phải số nguyên dương
    return True  # Trả về True nếu số căn cước hợp lệ

def is_valid_id_number_f(iid_number):
    # Kiểm tra xem số căn cước có đúng định dạng hay không
    # Đảm bảo id_number không chứa ký tự đặc biệt, không có khoảng trắng, là số nguyên dương và không trùng với id_number khác
    if not iid_number:
        print("Lỗi: Số CCCD không được để trống")
        return False  # Trả về False nếu tên rỗng
    if not iid_number.isdigit():
        print("Lỗi: Số căn cước chỉ được chứa chữ số")
        return False  # Trả về False nếu không phải toàn chữ số
    if ' ' in iid_number:
        print("Lỗi: Số căn cước không được chứa khoảng trắng")
        return False  # Trả về False nếu có khoảng trắng
    if int(iid_number) <= 0:
        print("Lỗi: Số căn cước phải là số nguyên dương")
        return False  # Trả về False nếu không phải số nguyên dương
    if data.find_student(id_number=iid_number):
        print("Lỗi: Số căn cước đã tồn tại trong danh sách khác")
        return False  # Trả về False nếu số căn cước đã tồn tại trong danh sách khác
    return True  # Trả về True nếu số căn cước hợp lệ

def is_valid_candidate_number(icandidate_number):
    if not icandidate_number:
        print("Lỗi: Số báo danh không được để trống")
        return False  # Trả về False nếu tên rỗng
    if ' ' in icandidate_number:
        print("Lỗi: Số báo danh không được chứa khoảng trắng")
        return False  # Trả về False nếu có khoảng trắng
    if not icandidate_number.startswith('S'):
        print("Lỗi: Số báo danh phải bắt đầu bằng 'S'")
        return False  # Trả về False nếu không bắt đầu bằng 'S'
    num_part = icandidate_number[1:]
    if not num_part.isdigit() or int(num_part) <= 0:
        print("Lỗi: Phần sau 'S' phải là số nguyên dương")
        return False  # Trả về False nếu phần sau 'S' không phải là số nguyên dương
    return True  # Trả về True nếu số báo danh hợp lệ

def is_valid_candidate_number_f(icandidate_number):
    if not icandidate_number:
        print("Lỗi: Số báo danh không được để trống")
        return False  # Trả về False nếu tên rỗng
    if ' ' in icandidate_number:
        print("Lỗi: Số báo danh không được chứa khoảng trắng")
        return False  # Trả về False nếu có khoảng trắng
    if not icandidate_number.startswith('S'):
        print("Lỗi: Số báo danh phải bắt đầu bằng 'S'")
        return False  # Trả về False nếu không bắt đầu bằng 'S'
    num_part = icandidate_number[1:]
    if not num_part.isdigit() or int(num_part) <= 0:
        print("Lỗi: Phần sau 'S' phải là số nguyên dương")
        return False  # Trả về False nếu phần sau 'S' không phải là số nguyên dương
    if data.find_student(candidate_number=icandidate_number):
        print("Lỗi: Số báo danh đã tồn tại trong danh sách sinh viên")
        return False  # Trả về False nếu số báo danh đã tồn tại trong danh sách khác
    return True  # Trả về True nếu số báo danh hợp lệ


def is_valid_name(iname):
    # Kiểm tra xem tên có đúng định dạng hay không
    if not isinstance(iname, str):
        print("Lỗi: Tên phải là chuỗi")
        return False  # Trả về False nếu không phải là chuỗi
    if not iname:
        print("Lỗi: Tên không được để trống")
        return False  # Trả về False nếu tên rỗng
    if any(not char.isalnum() and char != " " for char in iname):
        print("Lỗi: Tên không được chứa ký tự đặc biệt hoặc số")
        return False  # Trả về False nếu tên chứa ký tự đặc biệt hoặc số
    return True  # Trả về True nếu tên hợp lệ


def is_valid_address(iaddress):
    # Kiểm tra xem địa chỉ có đúng định dạng hay không
    if not isinstance(iaddress, str):
        print("Lỗi: Địa chỉ phải là chuỗi")
        return False  # Trả về False nếu không phải là chuỗi
    if not iaddress.strip():
        print("Lỗi: Địa chỉ không được để trống")
        return False  # Trả về False nếu địa chỉ rỗng
    if any(not char.isalnum() and char not in [',', '-', ' '] for char in iaddress):
        print("Lỗi: Địa chỉ không được chứa ký tự đặc biệt")
        return False  # Trả về False nếu địa chỉ chứa ký tự đặc biệt
    return True  # Trả về True nếu địa chỉ hợp lệ

def is_valid_subject(isubject):
    # Kiểm tra xem môn học có đúng định dạng hay không
    if isinstance(isubject, (int, float)):
        if 0 <= isubject <= 10:
            return True
        else:
            print("Lỗi: Môn học phải là số từ 0 đến 10")
            return False  # Trả về False nếu không nằm trong khoảng từ 0 đến 10
    else:
        print("Lỗi: Môn học phải là số nguyên hoặc số thực")
        return False  # Trả về False nếu không phải là số nguyên hoặc số thực




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
            while True:
                id_number = input('Nhập số CCCD: ')
                if not is_valid_id_number_f(id_number):
                    print("Vui lòng nhập lại.")
                else:
                    break  # Thoát khỏi vòng lặp nếu số CCCD hợp lệ

            while True:
                candidate_number = input('Nhập số báo danh: ')
                if not is_valid_candidate_number_f(candidate_number):
                    print("Vui lòng nhập lại.")
                else:
                    break
            
            while True:
                name = input('Nhập họ và tên: ')
                if not is_valid_name(name):
                    print("Vui lòng nhập lại.")
                else:
                    break

            while True:
                address = input('Nhập địa chỉ: ')
                if not is_valid_address(address):
                    print("Vui lòng nhập lại.")
                else:
                    break
            
            student_type = input('Khối thí sinh (A hoặc B): ')
            if student_type == 'A' or student_type == 'a':
                while True:
                    math = float(input('Nhập điểm toán: '))
                    if not is_valid_subject(math):
                        print("Vui lòng nhập lại.")
                    else:
                        break

                while True:
                    physics = float(input('Nhập điểm lý: '))
                    if not is_valid_subject(physics):
                        print("Vui lòng nhập lại.")
                    else:
                        break

                while True:
                    chemistry = float(input('Nhập điểm hóa: '))
                    if not is_valid_subject(chemistry):
                        print("Vui lòng nhập lại.")
                    else:
                        break
                student = StudentA(id_number, candidate_number, name, address, math, physics, chemistry)
            elif student_type == 'B' or student_type == 'b':
                while True:
                    math = float(input('Nhập điểm toán: '))
                    if not is_valid_subject(math):
                        print("Vui lòng nhập lại.")
                    else:
                        break

                while True:
                    chemistry = float(input('Nhập điểm lý: '))
                    if not is_valid_subject(chemistry):
                        print("Vui lòng nhập lại.")
                    else:
                        break
                    
                while True:
                    biology = float(input('Nhập điểm hóa: '))
                    if not is_valid_subject(biology):
                        print("Vui lòng nhập lại.")
                    else:
                        break
                student = StudentB(id_number, candidate_number, name, address, math, chemistry, biology)

            data.add_student(student)
            print('Thêm thí sinh thành công')
            print()
            pass

        elif option == '2':#Tìm kiếm thí sinh
            while True:
                input_candidate_number = input("Nhập số báo danh của thí sinh cần tìm: ")
                if not is_valid_candidate_number(input_candidate_number):
                    print("Vui lòng nhập lại.")
                else:
                    break
            found_student = data.find_student(candidate_number=input_candidate_number)
            if found_student is not None:
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
                print("Không tìm thấy thí sinh với số báo danh trên.")
                input_id = input("Vui lòng nhập số CCCD của thí sinh để tìm : ")
                if not is_valid_id_number(input_candidate_number):
                    print("Vui lòng nhập lại.")
                else:
                    break
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
                    print("Thí sinh không tồn tại.")

            print()
            pass

        elif option == '3':#Sửa thông tin thí sinh
            while True:
                candidate_number = input("Nhập số báo danh của thí sinh : ")
                if not is_valid_candidate_number(candidate_number):
                    print("Vui lòng nhập lại.")
                else:
                    break

            while True:
                id_number = input('Nhập số CCCD: ')
                if not is_valid_id_number(id_number):
                    print("Vui lòng nhập lại.")
                else:
                    break  # Thoát khỏi vòng lặp nếu số CCCD hợp lệ

            if(data.find_student(candidate_number=candidate_number, id_number=id_number)):
                new_info = {}
                while True:
                    new_info['name'] = input("Nhập tên mới của thí sinh : ")
                    if not is_valid_name(new_info['name']):
                        print("Vui lòng nhập lại.")
                    else:
                        break

                while True:
                    new_info['address'] = input("Nhập địa chỉ mới của thí sinh : ")
                    if not is_valid_address(new_info['address']):
                        print("Vui lòng nhập lại.")
                    else:
                        break

                exam_type = input("Nhập khối (A hoặc B): ")
                if exam_type == "A" or 'a':
                    while True:
                        new_info['math'] = float(input("Nhập điểm toán mới của thí sinh  : ") )
                        if not is_valid_subject(new_info['math']):
                            print("Vui lòng nhập lại.")
                        else:
                            break

                    while True:
                        new_info['physics'] = float(input("Nhập điểm vật lý mới của thí sinh  : ") )
                        if not is_valid_subject(new_info['physics']):
                            print("Vui lòng nhập lại.")
                        else:
                            break

                    while True:
                        new_info['chemistry'] = float(input("Nhập điểm hóa học mới của thí sinh  : ") )
                        if not is_valid_subject(new_info['chemistry']):
                            print("Vui lòng nhập lại.")
                        else:
                            break

                elif exam_type == "B" or 'b':
                    while True:
                        new_info['math'] = float(input("Nhập điểm toán mới của thí sinh  : ") )
                        if not is_valid_subject(new_info['chemistry']):
                            print("Vui lòng nhập lại.")
                        else:
                            break
                            
                    while True:
                        new_info['chemistry'] = float(input("Nhập điểm hóa học mới của thí sinh  : ") )
                        if not is_valid_subject(new_info['chemistry']):
                            print("Vui lòng nhập lại.")
                        else:
                            break
                    
                    while True:
                        new_info['biology'] = float(input("Nhập điểm toán mới của thí sinh  : ") )
                        if not is_valid_subject(new_info['biology']):
                            print("Vui lòng nhập lại.")
                        else:
                            break
                else:
                    print("Không tìm thấy thí sinh .")
                data.update_student(candidate_number, id_number, new_info)
                print("Sửa thông tin thành công")
            else:
                print("Thí sinh không tồn tại.")

            print()
            pass

        elif option == '4':#Xóa thí sinh
            while True:
                input_candidate_number = input("Nhập số báo danh của thí sinh cần xóa: ")
                if not is_valid_id_number(id_number):
                    print("Vui lòng nhập lại.")
                else:
                    break  # Thoát khỏi vòng lặp nếu số CCCD hợp lệ
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