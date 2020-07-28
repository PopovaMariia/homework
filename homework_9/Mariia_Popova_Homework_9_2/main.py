# Убрать лишний код, выделить отдельные части,вынести их в функции и заускать через if __name__ == ...


import random
from compare import compare
from validation import validation
from restart import restart

random_number = random.randint(1, 50)


def game():
    while True:
        user_number = input('Введите число:')
        for i in range(9):
            if validation(user_number) == 'Fail':
                return 'You need to use only numbers'
            compare(user_number, random_number)
            if compare(user_number, random_number) == 'You win':
                print('Вы угадали')
                break
            elif compare(user_number, random_number) == 'Вваше число Больше':
                user_number = input(f'Вваше число Больше. Осталось {9 - i} попыток: ')
            else:
                user_number = input(f'Вваше число Меньше. Осталось {9 - i} попыток: ')
        if restart() == 'yes':
            continue
        break
    return 'Игра закончилась'


if __name__ == '__main__':
    print(game())
