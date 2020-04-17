#!/usr/bin/env python
import copy


def main():
    grade_book1 = GradeBook()

    grade_book1.add_new_student(1, Student("Harry", "Potter"))
    grade_book1.add_new_student(2, Student("Mickey", "Mouse"))
    grade_book1.add_new_student(3, Student("Luke", "Sky Walker"))

    grade_book1.add_new_grade(3, "Biology", 5, 1.2)
    grade_book1.add_new_grade(3, "Chemistry", 4.5, 1.3)
    grade_book1.add_new_grade(1, "Physics", 4.0, 1.5)
    grade_book1.add_new_grade(1, "English", 4.0, 0.8)

    grade_book1.get_students_grades(3)

    grade_book2 = grade_book1.clone()
    grade_book2.add_new_grade(1, "Geography", 4.1, 0.9)

    grade_book1.get_all_students_average()
    grade_book2.get_all_students_average()


class Student:
    name = ""
    sure_name = ""

    def __init__(self, name, sure_name):
        self.name = name
        self.sure_name = sure_name
        pass


class GradeBook:
    def __init__(self):
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
        print("Average: {:.2f}".format(grades_value / grades_num))

    def clone(self):
        return copy.deepcopy(self)

    def get_students_grades(self, student_id: int):
        print("Student: {} {}:".format(self.students[student_id]['data'].name,
                                       self.students[student_id]['data'].sure_name))
        for subject in self.students[student_id]['grades']:
            print("Subject: {}, grade: {}".format(subject, self.students[student_id]['grades'][subject]['grade']))

    pass


if __name__ == '__main__':
    main()
