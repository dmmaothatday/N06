

from ManageStudents import ManageStudents
from Student import StudentA, StudentB

data = ManageStudents()
data.add_new_student(StudentA('05','5','a','hn',10,10,10))
data.add_new_student(StudentB('06','6','b','hn',1,2,3))
data.add_new_student(StudentA('07','7','c','hn',1,1,1))
# data.add_new_student(StudentB('4','S4','d','hn',2,2,2))
# data.add_new_student(StudentA('5','S5','f','hn',3,4,5))
# data.add_new_student(StudentA('6','S6','a','hn',10,10,10))
# data.add_new_student(StudentA('7','S7','a','hn',10,10,10))
# data.add_new_student(StudentA('8','S8','a','hn',10,10,10))
# data.add_new_student(StudentA('9','S9','a','hn',10,10,10))
# data.add_new_student(StudentA('10','S10','a','hn',10,10,10))
# data.add_new_student(StudentA('11','S11','a','hn',10,10,10))

def is_valid_cccd(icccd):
    # Loại bỏ dấu cách trong chuỗi CCCD
    icccd = icccd.replace(" ", "")
    
    # Kiểm tra xem CCCD có chứa ký tự đặc biệt hay không
    if not icccd.isalnum():
        print("CCCD không được chứa ký tự đặc biệt.")
        return False
    if not icccd.isdigit():
        print("Lỗi: CCCD chỉ được chứa số nguyên ")
        return False
    # Kiểm tra xem CCCD bắt đầu bằng số 0 hay không và có đúng 9 ký tự hay không
    if  icccd[0] != "0":
        print("CCCD phải bắt đầu bằng số 0 ")
        return False
    
    return True


def is_valid_cccd_f(icccd):
    # Loại bỏ dấu cách trong chuỗi CCCD
    icccd = icccd.replace(" ", "")
    
    # Kiểm tra xem CCCD có chứa ký tự đặc biệt hay không
    if not icccd.isalnum():
        print("CCCD không được chứa ký tự đặc biệt.")
        return False
    if not icccd.isdigit():
        print("Lỗi: CCCD chỉ được chứa số nguyên ")
        return False
    # Kiểm tra xem CCCD bắt đầu bằng số 0 hay không và có đúng 9 ký tự hay không
    if  icccd[0] != "0":
        print("CCCD phải bắt đầu bằng số 0 ")
        return False
    if data.search_student(cccd=icccd):
        print("Lỗi: Số CCCD đã tồn tại trong danh sách khác")
        return False  # Trả về False nếu số CCCD đã tồn tại trong danh sách khác
    return True  # Trả về True nếu số CCCD hợp lệ

def is_valid_sbd(isbd):
    # Loại bỏ dấu cách trong chuỗi SBD
    isbd = isbd.replace(" ", "")
    # Kiểm tra xem SBD chứa ký tự đặc biệt hay không
    if not isbd.isdigit():
        print("Lỗi: SBD chỉ được chứa số nguyên và không chứa ký tự đặc biệt.")
        return False
    return True



def is_valid_sbd_f(isbd):
    # Loại bỏ dấu cách trong chuỗi SBD
    isbd = isbd.replace(" ", "")
    # Kiểm tra xem SBD chứa ký tự đặc biệt hay không
    if not isbd.isdigit():
        print("Lỗi: SBD chỉ được chứa số nguyên và không chứa ký tự đặc biệt.")
        return False
    if data.search_student(sbd=isbd):
        print("Lỗi: Số báo danh đã tồn tại trong danh sách sinh viên")
        return False  # Trả về False nếu số báo danh đã tồn tại trong danh sách khác
    return True  # Trả về True nếu số báo danh hợp lệ


def is_valid_name(iho_ten):
    # Loại bỏ dấu cách ở đầu và cuối chuỗi tên
    iho_ten = iho_ten.strip()

    # Tách tên thành các từ và kiểm tra xem các từ có phải chỉ chứa chữ cái hay không
    words = iho_ten.split()
    for word in words:
        if not word.isalpha():
            print("Lỗi: Tên chỉ được chứa chữ cái và không chứa ký tự đặc biệt hoặc số.")
            return False
    
    return True




def is_valid_address(idia_chi):
    # Loại bỏ dấu cách ở đầu và cuối chuỗi địa chỉ
    idia_chi = idia_chi.strip()

    # Tách địa chỉ thành các từ và kiểm tra xem các từ có phải chỉ chứa chữ cái hay không
    words = idia_chi.split()
    for word in words:
        if not word.isalpha():
            print("Lỗi: Địa chỉ chỉ được chứa chữ cái và không chứa ký tự đặc biệt hoặc số.")
            return False
    
    return True



def is_valid_mon(imon):
    # Loại bỏ khoảng trống trong chuỗi môn học
    imon = imon.replace(" ", "")

    # Kiểm tra xem imon có đúng định dạng và chỉ chứa số nguyên hoặc số thực hay không
    if imon.replace(".", "", 1).isdigit():
        return True
    else:
        print("Lỗi: Môn học phải là số nguyên hoặc số thực và không chứa ký tự chữ.")
        return False



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
        choice = input('Vui lòng chọn chức năng (1-8): ')
        print()

        if choice == '1': #Thêm mới thí sinh
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
            while True:
                block = input('Khối thí sinh (A hoặc B): ')
                if block == 'A' or block == 'a':
                    while True:
                        diem_toan = input('Nhập điểm toán: ')
                        if not is_valid_mon(diem_toan):
                            print("Vui lòng nhập lại.")
                        else:
                            break

                    while True:
                        diem_ly = input('Nhập điểm lý: ')
                        if not is_valid_mon(diem_ly):
                            print("Vui lòng nhập lại.")
                        else:
                            break

                    while True:
                        diem_hoa = input('Nhập điểm hóa: ')
                        if not is_valid_mon(diem_hoa):
                            print("Vui lòng nhập lại.")
                        else:
                            break
                    student = StudentA(cccd, sbd, ho_ten, dia_chi, diem_toan, diem_ly, diem_hoa)
                    break
                elif block == 'B' or block == 'b':
                    while True:
                        diem_toan = input('Nhập điểm toán: ')
                        if not is_valid_mon(diem_toan):
                            print("Vui lòng nhập lại.")
                        else:
                            break

                    while True:
                        diem_hoa = input('Nhập điểm lý: ')
                        if not is_valid_mon(diem_hoa):
                            print("Vui lòng nhập lại.")
                        else:
                            break
                        
                    while True:
                        mon_sinh = input('Nhập điểm hóa: ')
                        if not is_valid_mon(mon_sinh):
                            print("Vui lòng nhập lại.")
                        else:
                            break
                    student = StudentB(cccd, sbd, ho_ten, dia_chi, diem_toan, diem_hoa, mon_sinh)
                    break
                else:
                    print("Không có khối đó")
            data.add_new_student(student)
            print('Thêm thí sinh thành công')
            print()
            pass

        elif choice == '2':#Tìm kiếm thí sinh
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
                    print("Điểm Sinh học:", found_student.mon_sinh)
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
                        print("Điểm Sinh học:", found_by_id.mon_sinh)
                else:
                    print("Thí sinh không tồn tại.")

            print()
            pass

        elif choice == '3':#Sửa thông tin thí sinh
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
                        new_info['diem_toan'] = input("Nhập điểm toán mới của thí sinh  : ") 
                        if not is_valid_mon(new_info['diem_toan']):
                            print("Vui lòng nhập lại.")
                        else:
                            break

                    while True:
                        new_info['diem_ly'] = input("Nhập điểm vật lý mới của thí sinh  : ") 
                        if not is_valid_mon(new_info['diem_ly']):
                            print("Vui lòng nhập lại.")
                        else:
                            break

                    while True:
                        new_info['diem_hoa'] = input("Nhập điểm hóa học mới của thí sinh  : ") 
                        if not is_valid_mon(new_info['diem_hoa']):
                            print("Vui lòng nhập lại.")
                        else:
                            break

                elif exam_type == "B" or 'b':
                    while True:
                        new_info['diem_toan'] = input("Nhập điểm toán mới của thí sinh  : ") 
                        if not is_valid_mon(new_info['diem_hoa']):
                            print("Vui lòng nhập lại.")
                        else:
                            break
                            
                    while True:
                        new_info['diem_hoa'] = input("Nhập điểm hóa học mới của thí sinh  : ") 
                        if not is_valid_mon(new_info['diem_hoa']):
                            print("Vui lòng nhập lại.")
                        else:
                            break
                    
                    while True:
                        new_info['mon_sinh'] = input("Nhập điểm toán mới của thí sinh  : ") 
                        if not is_valid_mon(new_info['mon_sinh']):
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

        elif choice == '4':#Xóa thí sinh
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

        # elif choice == '5':# Hiển thị danh sách thí sinh có điểm để xét vào đại học
        #     order = input("Nhập 'asc' để sắp xếp thứ tự từ thấp đến cao, hoặc 'desc' để sắp xếp từ cao đến thấp: ")
        #     sorted_students = data.sort_student_list_by_total_score(order)
        #     for student in sorted_students:
        #         print(f"cccd: {student.cccd}, ho_ten: {student.ho_ten}, score: {data.calculate_score(student)}")
        #     print()
        #     pass

        # elif choice == '6':# Hiển thị danh sách thí sinh đạt học bổng
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

        # elif choice == '7':# Hiển thị danh sách thí sinh không liệt môn nào
        #     students_without_failed_mons = data.get_student_list_without_failed_mons()
        #     if students_without_failed_mons is not None:
        #         for student in students_without_failed_mons:
        #             if isinstance(student, StudentA):
        #                 print(f"Tên: {student.ho_ten}, Toán: {student.diem_toan}, Lý: {student.diem_ly}, Hóa: {student.diem_hoa}")
        #             elif isinstance(student, StudentB):
        #                 print(f"Tên: {student.ho_ten}, Toán: {student.diem_toan}, Hóa: {student.diem_hoa}, Sinh: {student.mon_sinh}")
        #     else:
        #         print("không có thí sinh trượt.")
        #     pass
        elif choice == '8':
            print('Thoát chương trình')
            break
        else:
            print('Lựa chọn không hợp lệ, vui lòng chọn lại')
