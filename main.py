from ManageStudents import ManageStudents
from Student import StudentA, StudentB

data = ManageStudents()
data.add_new_student(StudentA('1','S1','a','hn',10,10,10))
data.add_new_student(StudentB('2','S2','b','hn',1,2,3))
data.add_new_student(StudentA('3','S3','c','hn',1,1,1))
# data.add_new_student(StudentB('4','S4','d','hn',2,2,2))
# data.add_new_student(StudentA('5','S5','f','hn',3,4,5))
# data.add_new_student(StudentA('6','S6','a','hn',10,10,10))
# data.add_new_student(StudentA('7','S7','a','hn',10,10,10))
# data.add_new_student(StudentA('8','S8','a','hn',10,10,10))
# data.add_new_student(StudentA('9','S9','a','hn',10,10,10))
# data.add_new_student(StudentA('10','S10','a','hn',10,10,10))
# data.add_new_student(StudentA('11','S11','a','hn',10,10,10))

def is_valid_cccd(icccd):
    # Kiểm tra xem số căn cước có đúng định dạng hay không
    # Đảm bảo cccd không chứa ký tự đặc biệt, không có khoảng trắng, là số nguyên dương và không trùng với cccd khác
    if not icccd:
        print("Lỗi: Số CCCD không được để trống")
        return False  # Trả về False nếu tên rỗng
    if not icccd.isdigit():
        print("Lỗi: Số căn cước chỉ được chứa chữ số")
        return False  # Trả về False nếu không phải toàn chữ số
    if ' ' in icccd:
        print("Lỗi: Số căn cước không được chứa khoảng trắng")
        return False  # Trả về False nếu có khoảng trắng
    if int(icccd) <= 0:
        print("Lỗi: Số căn cước phải là số nguyên dương")
        return False  # Trả về False nếu không phải số nguyên dương
    return True  # Trả về True nếu số căn cước hợp lệ

def is_valid_cccd_f(icccd):
    # Kiểm tra xem số căn cước có đúng định dạng hay không
    # Đảm bảo cccd không chứa ký tự đặc biệt, không có khoảng trắng, là số nguyên dương và không trùng với cccd khác
    if not icccd:
        print("Lỗi: Số CCCD không được để trống")
        return False  # Trả về False nếu tên rỗng
    if not icccd.isdigit():
        print("Lỗi: Số căn cước chỉ được chứa chữ số")
        return False  # Trả về False nếu không phải toàn chữ số
    if ' ' in icccd:
        print("Lỗi: Số căn cước không được chứa khoảng trắng")
        return False  # Trả về False nếu có khoảng trắng
    if int(icccd) <= 0:
        print("Lỗi: Số căn cước phải là số nguyên dương")
        return False  # Trả về False nếu không phải số nguyên dương
    if data.search_student(cccd=icccd):
        print("Lỗi: Số căn cước đã tồn tại trong danh sách khác")
        return False  # Trả về False nếu số căn cước đã tồn tại trong danh sách khác
    return True  # Trả về True nếu số căn cước hợp lệ

def is_valid_sbd(isbd):
    if not isbd:
        print("Lỗi: Số báo danh không được để trống")
        return False  # Trả về False nếu tên rỗng
    if ' ' in isbd:
        print("Lỗi: Số báo danh không được chứa khoảng trắng")
        return False  # Trả về False nếu có khoảng trắng
    if not isbd.startswith('S'):
        print("Lỗi: Số báo danh phải bắt đầu bằng 'S'")
        return False  # Trả về False nếu không bắt đầu bằng 'S'
    num_part = isbd[1:]
    if not num_part.isdigit() or int(num_part) <= 0:
        print("Lỗi: Phần sau 'S' phải là số nguyên dương")
        return False  # Trả về False nếu phần sau 'S' không phải là số nguyên dương
    return True  # Trả về True nếu số báo danh hợp lệ

def is_valid_sbd_f(isbd):
    if not isbd:
        print("Lỗi: Số báo danh không được để trống")
        return False  # Trả về False nếu tên rỗng
    if ' ' in isbd:
        print("Lỗi: Số báo danh không được chứa khoảng trắng")
        return False  # Trả về False nếu có khoảng trắng
    if not isbd.startswith('S'):
        print("Lỗi: Số báo danh phải bắt đầu bằng 'S'")
        return False  # Trả về False nếu không bắt đầu bằng 'S'
    num_part = isbd[1:]
    if not num_part.isdigit() or int(num_part) <= 0:
        print("Lỗi: Phần sau 'S' phải là số nguyên dương")
        return False  # Trả về False nếu phần sau 'S' không phải là số nguyên dương
    if data.search_student(sbd=isbd):
        print("Lỗi: Số báo danh đã tồn tại trong danh sách sinh viên")
        return False  # Trả về False nếu số báo danh đã tồn tại trong danh sách khác
    return True  # Trả về True nếu số báo danh hợp lệ


def is_valid_name(iho_ten):
    # Kiểm tra xem tên có đúng định dạng hay không
    if not isinstance(iho_ten, str):
        print("Lỗi: Tên phải là chuỗi")
        return False  # Trả về False nếu không phải là chuỗi
    if not iho_ten:
        print("Lỗi: Tên không được để trống")
        return False  # Trả về False nếu tên rỗng
    if any(not char.isalnum() and char != " " for char in iho_ten):
        print("Lỗi: Tên không được chứa ký tự đặc biệt hoặc số")
        return False  # Trả về False nếu tên chứa ký tự đặc biệt hoặc số
    return True  # Trả về True nếu tên hợp lệ


def is_valid_address(idia_chi):
    # Kiểm tra xem địa chỉ có đúng định dạng hay không
    if not isinstance(idia_chi, str):
        print("Lỗi: Địa chỉ phải là chuỗi")
        return False  # Trả về False nếu không phải là chuỗi
    if not idia_chi.strip():
        print("Lỗi: Địa chỉ không được để trống")
        return False  # Trả về False nếu địa chỉ rỗng
    if any(not char.isalnum() and char not in [',', '-', ' '] for char in idia_chi):
        print("Lỗi: Địa chỉ không được chứa ký tự đặc biệt")
        return False  # Trả về False nếu địa chỉ chứa ký tự đặc biệt
    return True  # Trả về True nếu địa chỉ hợp lệ

def is_valid_mon(imon):
    # Kiểm tra xem môn học có đúng định dạng hay không
    if isinstance(imon, (int, float)):
        if 0 <= imon <= 10:
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
                cccd = input('Nhập số CCCD: ')
                if not is_valid_cccd_f(cccd):
                    print("Vui lòng nhập lại.")
                else:
                    break  # Thoát khỏi vòng lặp nếu số CCCD hợp lệ

            while True:
                sbd = input('Nhập số báo danh: ')
                if not is_valid_sbd_f(sbd):
                    print("Vui lòng nhập lại.")
                else:
                    break
            
            while True:
                ho_ten = input('Nhập họ và tên: ')
                if not is_valid_name(ho_ten):
                    print("Vui lòng nhập lại.")
                else:
                    break

            while True:
                dia_chi = input('Nhập địa chỉ: ')
                if not is_valid_address(dia_chi):
                    print("Vui lòng nhập lại.")
                else:
                    break
            
            student_type = input('Khối thí sinh (A hoặc B): ')
            if student_type == 'A' or student_type == 'a':
                while True:
                    diem_toan = float(input('Nhập điểm toán: '))
                    if not is_valid_mon(diem_toan):
                        print("Vui lòng nhập lại.")
                    else:
                        break

                while True:
                    diem_ly = float(input('Nhập điểm lý: '))
                    if not is_valid_mon(diem_ly):
                        print("Vui lòng nhập lại.")
                    else:
                        break

                while True:
                    diem_hoa = float(input('Nhập điểm hóa: '))
                    if not is_valid_mon(diem_hoa):
                        print("Vui lòng nhập lại.")
                    else:
                        break
                student = StudentA(cccd, sbd, ho_ten, dia_chi, diem_toan, diem_ly, diem_hoa)
            elif student_type == 'B' or student_type == 'b':
                while True:
                    diem_toan = float(input('Nhập điểm toán: '))
                    if not is_valid_mon(diem_toan):
                        print("Vui lòng nhập lại.")
                    else:
                        break

                while True:
                    diem_hoa = float(input('Nhập điểm lý: '))
                    if not is_valid_mon(diem_hoa):
                        print("Vui lòng nhập lại.")
                    else:
                        break
                    
                while True:
                    biology = float(input('Nhập điểm hóa: '))
                    if not is_valid_mon(biology):
                        print("Vui lòng nhập lại.")
                    else:
                        break
                student = StudentB(cccd, sbd, ho_ten, dia_chi, diem_toan, diem_hoa, biology)

            data.add_new_student(student)
            print('Thêm thí sinh thành công')
            print()
            pass

        elif option == '2':#Tìm kiếm thí sinh
            while True:
                input_sbd = input("Nhập số báo danh của thí sinh cần tìm: ")
                if not is_valid_sbd(input_sbd):
                    print("Vui lòng nhập lại.")
                else:
                    break
            found_student = data.search_student(sbd=input_sbd)
            if found_student is not None:
                print("Số CMND:", found_student.cccd)
                print("Số báo danh:", found_student.sbd)
                print("Tên:", found_student.ho_ten)
                print("Địa chỉ:", found_student.dia_chi)
                if isinstance(found_student, StudentA):
                    print("Điểm Toán:", found_student.diem_toan)
                    print("Điểm Vật lý:", found_student.diem_ly)
                    print("Điểm Hóa học:", found_student.diem_hoa)
                elif isinstance(found_student, StudentB):
                    print("Điểm Toán:", found_student.diem_toan)
                    print("Điểm Hóa học:", found_student.diem_hoa)
                    print("Điểm Sinh học:", found_student.biology)
            else:
                print("Không tìm thấy thí sinh với số báo danh trên.")
                input_id = input("Vui lòng nhập số CCCD của thí sinh để tìm : ")
                if not is_valid_cccd(input_sbd):
                    print("Vui lòng nhập lại.")
                else:
                    break
                found_by_id = data.search_student(cccd=input_id)
                if found_by_id is not None:
                    print("Thông tin của thí sinh:")
                    print("Số CMND:", found_by_id.cccd)
                    print("Số báo danh:", found_by_id.sbd)  # Lưu ý sửa đổi đến chữ hoa/thường ở đây
                    print("Tên:", found_by_id.ho_ten)
                    print("Địa chỉ:", found_by_id.dia_chi)
                    if isinstance(found_by_id, StudentA):
                        print("Điểm Toán:", found_by_id.diem_toan)
                        print("Điểm Vật lý:", found_by_id.diem_ly)
                        print("Điểm Hóa học:", found_by_id.diem_hoa)
                    elif isinstance(found_by_id, StudentB):
                        print("Điểm Toán:", found_by_id.diem_toan)
                        print("Điểm Hóa học:", found_by_id.diem_hoa)
                        print("Điểm Sinh học:", found_by_id.biology)
                else:
                    print("Thí sinh không tồn tại.")

            print()
            pass

        elif option == '3':#Sửa thông tin thí sinh
            while True:
                sbd = input("Nhập số báo danh của thí sinh : ")
                if not is_valid_sbd(sbd):
                    print("Vui lòng nhập lại.")
                else:
                    break

            while True:
                cccd = input('Nhập số CCCD: ')
                if not is_valid_cccd(cccd):
                    print("Vui lòng nhập lại.")
                else:
                    break  # Thoát khỏi vòng lặp nếu số CCCD hợp lệ

            if(data.search_student(sbd=sbd, cccd=cccd)):
                new_info = {}
                while True:
                    new_info['ho_ten'] = input("Nhập tên mới của thí sinh : ")
                    if not is_valid_name(new_info['ho_ten']):
                        print("Vui lòng nhập lại.")
                    else:
                        break

                while True:
                    new_info['dia_chi'] = input("Nhập địa chỉ mới của thí sinh : ")
                    if not is_valid_address(new_info['dia_chi']):
                        print("Vui lòng nhập lại.")
                    else:
                        break

                exam_type = input("Nhập khối (A hoặc B): ")
                if exam_type == "A" or 'a':
                    while True:
                        new_info['diem_toan'] = float(input("Nhập điểm toán mới của thí sinh  : ") )
                        if not is_valid_mon(new_info['diem_toan']):
                            print("Vui lòng nhập lại.")
                        else:
                            break

                    while True:
                        new_info['diem_ly'] = float(input("Nhập điểm vật lý mới của thí sinh  : ") )
                        if not is_valid_mon(new_info['diem_ly']):
                            print("Vui lòng nhập lại.")
                        else:
                            break

                    while True:
                        new_info['diem_hoa'] = float(input("Nhập điểm hóa học mới của thí sinh  : ") )
                        if not is_valid_mon(new_info['diem_hoa']):
                            print("Vui lòng nhập lại.")
                        else:
                            break

                elif exam_type == "B" or 'b':
                    while True:
                        new_info['diem_toan'] = float(input("Nhập điểm toán mới của thí sinh  : ") )
                        if not is_valid_mon(new_info['diem_hoa']):
                            print("Vui lòng nhập lại.")
                        else:
                            break
                            
                    while True:
                        new_info['diem_hoa'] = float(input("Nhập điểm hóa học mới của thí sinh  : ") )
                        if not is_valid_mon(new_info['diem_hoa']):
                            print("Vui lòng nhập lại.")
                        else:
                            break
                    
                    while True:
                        new_info['biology'] = float(input("Nhập điểm toán mới của thí sinh  : ") )
                        if not is_valid_mon(new_info['biology']):
                            print("Vui lòng nhập lại.")
                        else:
                            break
                else:
                    print("Không tìm thấy thí sinh .")
                data.edit_student_info(sbd, cccd, new_info)
                print("Sửa thông tin thành công")
            else:
                print("Thí sinh không tồn tại.")

            print()
            pass

        elif option == '4':#Xóa thí sinh
            while True:
                input_sbd = input("Nhập số báo danh của thí sinh cần xóa: ")
                if not is_valid_sbd(input_sbd):
                    print("Vui lòng nhập lại.")
                else:
                    break  # Thoát khỏi vòng lặp nếu số CCCD hợp lệ
            found_student = data.search_student(sbd=input_sbd)
            if found_student is not None:
                data.delete_student(input_sbd)
                print("Đã xóa thông tin của thí sinh có số báo danh:", input_sbd)
            else:
                print("Số báo danh không tồn tại.")
            
            print()
            pass

        # elif option == '5':# Hiển thị danh sách thí sinh có điểm để xét vào đại học
        #     order = input("Nhập 'asc' để sắp xếp thứ tự từ thấp đến cao, hoặc 'desc' để sắp xếp từ cao đến thấp: ")
        #     sorted_students = data.sort_student_list_by_total_score(order)
        #     for student in sorted_students:
        #         print(f"cccd: {student.cccd}, ho_ten: {student.ho_ten}, score: {data.calculate_score(student)}")
        #     print()
        #     pass

        # elif option == '6':# Hiển thị danh sách thí sinh đạt học bổng
        #     students_with_scholarship = data.get_students_with_scholarship()
        #     if students_with_scholarship is not None:
        #         for student in students_with_scholarship:
        #             if isinstance(student, StudentA): #and data.calculate_score(student) >=32:
        #                 print(f"Tên: {student.ho_ten},  Điểm vào đại học: {data.calculate_score(student)}")
        #             elif isinstance(student, StudentB): #and data.calculate_score(student) >=32:
        #                 print(f"Tên: {student.ho_ten},  Điểm vào đại học: {data.calculate_score(student)}")
        #     else:
        #         print("Không có thí sinh nào đạt học bổng.")
        #     print()
        #     pass

        # elif option == '7':# Hiển thị danh sách thí sinh không liệt môn nào
        #     students_without_failed_mons = data.get_student_list_without_failed_mons()
        #     if students_without_failed_mons is not None:
        #         for student in students_without_failed_mons:
        #             if isinstance(student, StudentA):
        #                 print(f"Tên: {student.ho_ten}, Toán: {student.diem_toan}, Lý: {student.diem_ly}, Hóa: {student.diem_hoa}")
        #             elif isinstance(student, StudentB):
        #                 print(f"Tên: {student.ho_ten}, Toán: {student.diem_toan}, Hóa: {student.diem_hoa}, Sinh: {student.biology}")
        #     else:
        #         print("không có thí sinh trượt.")
        #     pass
        elif option == '8':
            print('Thoát chương trình')
            break
        else:
            print('Lựa chọn không hợp lệ, vui lòng chọn lại')