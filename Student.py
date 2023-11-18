class Student:
    def __init__(self, cccd, sbd, ho_ten, dia_chi):
        self.cccd = cccd
        self.sbd = sbd
        self.ho_ten = ho_ten
        self.dia_chi = dia_chi

    def get_cccd(self):
        return self.cccd

    def set_cccd(self, cccd):
        self.cccd = cccd

    def get_sbd(self):
        return self.sbd

    def set_sbd(self, sbd):
        self.sbd = sbd

    def get_ho_ten(self):
        return self.ho_ten

    def set_ho_ten(self, ho_ten):
        self.ho_ten = ho_ten

    def get_dia_chi(self):
        return self.dia_chi

    def set_dia_chi(self, dia_chi):
        self.dia_chi = dia_chi


class StudentA(Student):
    def __init__(self, cccd, sbd, ho_ten, dia_chi, diem_toan, diem_ly, diem_hoa):
        super().__init__(cccd, sbd, ho_ten, dia_chi)
        self.diem_toan = diem_toan
        self.diem_ly = diem_ly
        self.diem_hoa = diem_hoa

    def get_diem_toan(self):
        return self.diem_toan

    def set_diem_toan(self, diem):
        self.diem_toan = diem

    def get_diem_ly(self):
        return self.diem_ly

    def set_diem_ly(self, diem):
        self.diem_ly = diem

    def get_diem_hoa(self):
        return self.diem_hoa

    def set_diem_hoa(self, diem):
        self.diem_hoa = diem


class StudentB(Student):
    def __init__(self, cccd, sbd, ho_ten, dia_chi, diem_toan, diem_ly, diem_hoa):
        super().__init__(cccd, sbd, ho_ten, dia_chi)
        self.diem_toan = diem_toan
        self.diem_ly = diem_ly
        self.diem_hoa = diem_hoa

    def get_diem_toan(self):
        return self.diem_toan

    def set_diem_toan(self, diem):
        self.diem_toan = diem

    def get_diem_hoa(self):
        return self.diem_hoa

    def set_diem_hoa(self, diem):
        self.diem_hoa = diem

    def get_diem_sinh(self):
        return self.diem_sinh

    def set_diem_sinh(self, diem):
        self.diem_sinh = diem