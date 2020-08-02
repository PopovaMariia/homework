"""
Написать игру. 2 игрока бросают игровые кубики по 10 раз,
нужно определить кто выиграл и вывести результаты обоих игроков (суммы бросков).
Если у двух игроков за 1 ход выпало на кубиках одинаковое число, то игроки перебрасывают кубики.
"""

from game import game

sum_player_1, sum_player_2 = game()


def result():
    if sum_player_1 > sum_player_2:
        return 'Player #1 won'
    elif sum_player_1 < sum_player_2:
        return 'Player #2 won'
    return 'Friendship won'

if __name__ == '__main__':
    print(result())
