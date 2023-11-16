from Student import StudentA, StudentB


class ManageStudents:
    def __init__(self):
        self.student_list = []

    def add_student(self, student):
        self.student_list.append(student)

    def update_student(self, candidate_number, id_number, new_info):
        for student in self.student_list:
            if student.candidate_number == candidate_number and student.id_number == id_number:
                for key, value in new_info.items():
                    setattr(student, key, value)
                return

    def delete_student(self, candidate_number):
        for student in self.student_list:
            if student.candidate_number == candidate_number:
                self.student_list.remove(student)

    def find_student(self, candidate_number=None, id_number=None):
        if candidate_number:
            for student in self.student_list:
                if student.candidate_number == candidate_number:
                    return student
        elif id_number:
            for student in self.student_list:
                if student.id_number == id_number:
                    return student
        return None

    def get_students_by_block(self, block):
        for student in self.student_list:
            if isinstance(student, StudentA) and block == 'A':
                print(student.name, student.block, student.math, student.physics, student.chemistry)
            elif isinstance(student, StudentB) and block == 'B':
                print(student.name, student.block, student.math, student.chemistry, student.biology)

    def calculate_score(self, student):
        if isinstance(student, StudentA):
            return student.math * 1.5 + student.physics + student.chemistry
        elif isinstance(student, StudentB):
            return student.math + student.chemistry + student.biology * 1.5

    def calculate_average_score(self, student):
        if isinstance(student, StudentA):
            return (student.math + student.physics + student.chemistry) / 3
        elif isinstance(student, StudentB):
            return (student.math + student.chemistry + student.biology) / 3

    def sort_student_list_by_total_score(self, order='desc'):
        if order == 'desc':
            return sorted(self.student_list, key=lambda x: self.calculate_score(x), reverse=True)
        elif order == 'asc':
            return sorted(self.student_list, key=lambda x: self.calculate_score(x))

    def get_student_list_without_failed_subjects(self):
        result = []
        for student in self.student_list:
            if isinstance(student, StudentA) and all(score >= 2 for score in [student.math, student.physics, student.chemistry]):
                result.append(student)
            elif isinstance(student, StudentB) and all(score >= 2 for score in [student.math, student.chemistry, student.biology]):
                result.append(student)
        return result

    def get_students_with_scholarship(self):
        result = []
        for student in self.student_list:
            if isinstance(student, StudentA) or isinstance(student, StudentB):
                if self.calculate_score(student) >= 32:
                    result.append(student)
        result = [student for student in self.sort_student_list_by_total_score('desc') if self.calculate_score(student) >= 32]
        return result[:5]



