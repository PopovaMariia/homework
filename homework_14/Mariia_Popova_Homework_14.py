"""Реализовать класс Person (два атрибута: age и name) с методами:
def know(self, another_person_object) который позволяет добавить другого человека
def is_known(self, another_person_object) который возвращает знакомы ли два человека"""


class Person():

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__friends = []

    def know(self, new_friend):
        self.__friends.append(new_friend)

    def is_known(self, new_friend):
        if new_friend in self.__friends:
            return True
        return False


pers_1 = Person('Vania', 33)
pers_2 = Person('Petia', 22)
pers_3 = Person('Fedia', 33)

pers_1.know(pers_2)
pers_2.know(pers_3)

print(pers_1.is_known(pers_2))  # True
print(pers_2.is_known(pers_3))  # True
print(pers_1.is_known(pers_3))  # False
