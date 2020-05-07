from .student import Student
import copy


class GradeBook:

    def __init__(self):
        super().__init__()
        self.students = {}

    def add_new_student(self, student_id: int, student: Student):
        self.students[student_id] = {}
        self.students[student_id]['grades'] = {}
        self.students[student_id]['data'] = student
        pass

    def add_new_grade(self, student_id: int, subject: str, grade: float, weight: float):
        self.students[student_id]['grades'][subject] = {}
        self.students[student_id]['grades'][subject]['grade'] = grade
        self.students[student_id]['grades'][subject]['weight'] = weight
        pass

    def get_all_students_average(self):
        grades_num = 0
        grades_value = 0
        for student_id in self.students:
            for subject in self.students[student_id]['grades']:
                grades_value = grades_value + (self.students[student_id]['grades'][subject]['grade'] *
                                               self.students[student_id]['grades'][subject]['weight'])
                grades_num = grades_num + 1
        if grades_num > 0:
            return "{:.2f}".format(grades_value / grades_num)
        else:
            return 0

    def clone(self):
        return copy.deepcopy(self)

    def get_students_grades(self, student_id: int):
        res = []
        try:
            res.append("Student: {} {}:".format(self.students[student_id]['data'].name,
                                                self.students[student_id]['data'].sure_name))
            for subject in self.students[student_id]['grades']:
                res.append(
                    "Subject: {}, grade: {}".format(subject, self.students[student_id]['grades'][subject]['grade']))
            return res
        except KeyError:
            return ['No grades for student id {id}'.format(id=student_id)]
        