def compare(user_number, random_number):
    if int(user_number) == random_number:
        return 'You win'
    elif int(user_number) > random_number:
        return 'Вваше число Больше'
    elif int(user_number) < random_number:
        return 'Вваше число Меньше'
