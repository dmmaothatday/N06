class Student:
    def __init__(self, id_number, candidate_number, name, address):
        self.id_number = id_number
        self.candidate_number = candidate_number
        self.name = name
        self.address = address

    def get_id_number(self):
        return self.id_number

    def set_id_number(self, value):
        self.id_number = value

    def get_candidate_number(self):
        return self.candidate_number

    def set_candidate_number(self, value):
        self.candidate_number = value

    def get_name(self):
        return self.name

    def set_name(self, value):
        self.name = value

    def get_address(self):
        return self.address

    def set_address(self, value):
        self.address = value

class StudentA(Student):
    def __init__(self, id_number, exam_number, name, address, math, physics, chemistry):
        super().__init__(id_number, exam_number, name, address)
        self.math = math
        self.physics = physics
        self.chemistry = chemistry

    def get_math(self):
        return self.math

    def set_math(self, value):
        self.math = value

    def get_physics(self):
        return self.physics

    def set_physics(self, value):
        self.physics = value

    def get_chemistry(self):
        return self.chemistry

    def set_chemistry(self, value):
        self.chemistry = value

class StudentB(Student):
    def __init__(self, id_number, exam_number, name, address, math, chemistry, biology):
        super().__init__(id_number, exam_number, name, address)
        self.math = math
        self.chemistry = chemistry
        self.biology = biology

    def get_math(self):
        return self.math

    def set_math(self, value):
        self.math = value

    def get_chemistry(self):
        return self.chemistry

    def set_chemistry(self, value):
        self.chemistry = value

    def get_biology(self):
        return self.biology

    def set_biology(self, value):
        self.biology = value
