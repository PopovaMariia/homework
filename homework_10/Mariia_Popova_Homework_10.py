"""
Input: Feb 12 2019 2:41PM
Output: 2019-02-12 14:41:00
Функция принимает строку (пример - Input) и возвращает строку (пример - Output)
"""
from datetime import datetime

date_input = "Feb 12 2019 2:41PM"
date_output = str(datetime.strptime(date_input, "%b %d %Y %I:%M%p"))

print(date_output)

"""
Напишите функция is_prime, которая принимает 1 аргумент (число) и возвращает True, если число простое, иначе False
Простое число - это число, которое делится без остатка только на себя и на 1
"""


def is_prime(number):
    if number > 1:
        for i in range(2, number // 2):
            if (number % i) == 0:
                return False
            return True
    return False


print(is_prime(13))

"""
Напишите функцию, которая принимает 1 аргумент (строка) и выполняет ... действия на каждую из букв строки
"""


def parse(rules):
    res = []
    value = 0
    for rule in rules:
        if rule == 'i':
            value += 1
        elif rule == 's':
            value *= value
        elif rule == 'd':
            value -= 1
        elif rule == 'o':
            res.append(value)
    return res


print(parse("iiisdoso"))
