"""
Суть задачи:
юзер пришел в казино, сел за автомат, начал игру и у него начали выпадать рандомно величины из представленных выше.
Нужно написать впрограмму, которая за каждым вводом "Играть" (на Ваше усмотрение) - делал вывод полученых очков в комбинации и количество очков 
юзера за всю игру. Если юзре ввел "Выйти" (на ваше усмотрение) - выходит из программы и показвает количество очков за игру.
Выше есть таблица со значениями сколько какая комбинация весит.
"""

start_game = input('Do you want to start? Write Y or N: ')
import score
from restart import restart


def total():
    res = 0
    while start_game == 'Y':
        res = res + score.score()
        print(f'You have', res, 'points')
        if restart() == 'yes':
            continue
        break
    return res


if __name__ == '__main__':
    print(f'Your total score', total())
