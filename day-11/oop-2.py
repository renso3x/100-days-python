from re import I


class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade # 0 - 100

    def get_grade(self):
        return self.grade

class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        
        return False

    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()

        return value / len(self.students)


s1 = Student("Romeo", 19, 95)
s2 = Student("Joy", 25, 99)
s3 = Student("Ricah", 12, 100)

bsit = Course("BSIT", 2)
bsit.add_student(s1)
print(bsit.add_student(s3)) #False
print(bsit.get_average_grade())