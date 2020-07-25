# 3 Угадать число
import random
import sys

random_number = random.randint(1, 50)
user_number = input('Please, write any number from 1 to 50 ')


def validation(user_number):
    if not isinstance(user_number, (str, int)):
        return 'Please use number'
    if isinstance(user_number, str) and user_number.isdigit():
        user_number = int(user_number)
    else:
        return 'Please use number'
    return


def compare():
    global user_number
    validation(user_number)
    for attempt in range(1, 10, 1):
        if user_number == random_number:
            return attempt
        user_number = input("Number: ")
    return sys.exit()


compare()

# 4 Сохраним последний успешный запуск
import json
import datetime

data = {'Number': user_number, 'Attemp': attempt, 'Date': str(datetime.datetime.today())}
with open('result.json', 'w') as file:
    json.dump(data, file, indent=4)
