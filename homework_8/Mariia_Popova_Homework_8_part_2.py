# 3 Угадать число
import random
from typing import Set

random_number = random.randint(1, 50)
user_number = 0
attempt = 1


def validation(user_number):
    if not isinstance(user_number, (str, int)):
        return 'Fail'
    if isinstance(user_number, str) and user_number.isdigit():
        user_number = int(user_number)
        return
    return 'Fail'


def compare():
    global user_number
    global attempt
    for attempt in range(10):
        if int(user_number) == random_number:
            return 'You won'
        user_number = input("Number: ")
        if validation(user_number) == 'Fail':
            return 'You need to use only numbers'
    return 'Game over'


print(f'Please, write any number from 1 to 50.')
print(compare())

# 4 Сохраним последний успешный запуск
import json
import datetime

data = {'Number': user_number, 'Attemp': attempt, 'Date': str(datetime.datetime.today())}
if validation(user_number) != 'Fail':
    if int(user_number) == random_number:
        with open('result.json', 'w') as file:
            json.dump(data, file, indent=4)
