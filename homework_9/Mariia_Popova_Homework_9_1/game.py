import random


def game():
    sum_player_1 = 0
    sum_player_2 = 0
    i = 1
    while i <= 10:
        player_1 = random.randint(1, 6)
        player_2 = random.randint(1, 6)
        if player_1 == player_2:
            i = i
            continue
        sum_player_1 = sum_player_1 + player_1
        sum_player_2 = sum_player_2 + player_2
        i += 1
    return sum_player_1, sum_player_2
