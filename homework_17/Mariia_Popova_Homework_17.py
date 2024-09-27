class Student:
    def __init__(self, exam_book, name, grades):
        self.exam_book = exam_book
        self.name = name
        self.grades = grades
        self.student = {self.exam_book: (self.name, self.grades)}


    def add_student(self):
        group = {}
        group.update(self.student)
        print(group)
        return group


    def __str__(self):
        return f'{self.name}'

class Group:
    def __init__(self, name_group):
        self.name = name_group
        # self.group =

alex = Student(1304, 'Alex', 97)
mariia = Student(2109, 'Mariia', 90)
dariia = Student(1304,'Dariia', 100)

group_dm = (alex, mariia, dariia)
while True:
    for student in group_dm:
        student.add_student()
    break