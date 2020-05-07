from models.student import Student
from .abstract_controller import AbstractController


class GradeBookController(AbstractController):
    def __init__(self, model=None, view=None):
        super().__init__(model, view)

    def get_user_input(self):
        try:
            obj = input('''
            (s) Add new student
            (g) Add new grade
            (a) Get students average
            (l) List student's grades
            ''')
            if obj == 'q':
                return False
            elif obj == 's':
                # self.model.modify()
                self.add_new_student()
            elif obj == 'g':
                self.add_new_grade()
            elif obj == 'a':
                self.get_all_students_average()
            elif obj == 'l':
                self.get_students_grades()
            else:
                print('Incorrect value')
            return True
        except ValueError:
            print("Error: try again")
            return True

    def add_new_student(self):
        name, sure_name, student_id = input('Type: name, sure_name, id (coma separated)\n').split(",")
        student = Student(name, sure_name)
        self.model.add_new_student(student_id, student)

    def add_new_grade(self):
        student_id, subject, grade, weight = input('Type: id, subject, grade, weight (coma separated)\n').split(",")
        self.model.add_new_grade(student_id, subject, grade, weight)

    def get_all_students_average(self):
        print(self.model.get_all_students_average())

    def get_students_grades(self):
        student_id = input('Type student id\n')
        for line in self.model.get_students_grades(student_id):
            print(line)