from .abstract_model import AbstractModel
from models.gradebook import GradeBook


class GradeBookModel(AbstractModel):
    def __init__(self):
        self.grade_book = GradeBook()
        super().__init__()
        self.__current_output = ''

    def modify(self, *args, **kwargs):
        self.__current_output = args[0]
        self.notify()

    def notify(self):
        for obs in self._obs_list.values():
            obs.update(self.__current_output)

    def get_all_students_average(self):
        return self.grade_book.get_all_students_average()

    def add_new_student(self, student_id, student):
        return self.grade_book.add_new_student(student_id, student)

    def add_new_grade(self, student_id, subject, grade, weight):
        return self.grade_book.add_new_grade(student_id, subject, int(grade), float(weight))

    def get_students_grades(self, student_id):
        return self.grade_book.get_students_grades(student_id)
    