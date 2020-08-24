
class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def as_dict(self):
        return {
            'name': self.name,
            'age': int(self.age),
            'grades': int(self.grades),
        }


class Group:
    def __init__(self, name_group):
        self.name_group = name_group
        self.group = self.load_group()

    def load_group(self):
        try:
            with open(f'{self.name_group}.json', 'r') as file:
                data = json.load(file)
                group = []
                for student in data:
                    group.append(Student(student['name'], student['age'], student['grades']))
                return group
        except FileNotFoundError:
            return []

    @property
    def group_list(self):
        group = ''
        for name, student in enumerate(self.group):
            group += f'\n {name}\t {student.name}\t {student.age}\t {student.grades}'
        return group

    def add_student(self, student):
        self.group.append(student)

    def check_student(self, name):
        try:
            name in self.group[name].name
        except Exception:
            return False

def init_name_group():
    name_group = input('group ')
    return Group(name_group)


def main():
    name_group = init_name_group()
    try:
        while True:
            action = input('Action with list ')
            if action == 'Add_student':
                name = input('Name: ')
                if name_group.check_student(name) == True:
                    print('Such student has already been in the list')
                    continue
                print(name_group.check_student(name))
                age = int(input('Age: '))
                grades = int(input('Grades: '))
                name_group.add_student(Student(name, age, grades))
    except Exception:
        name_group.to_json()


if __name__ == '__main__':
    main()