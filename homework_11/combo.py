import random


def combo():
    wheel = {"A": 9, "B": 8, "C": 7, "D": 6, "E": 5, "F": 4, "G": 3, "H": 2, "I": 1, "XXX": 10}
    combo = []

    for i in range(3):
        wheel_list = list(wheel)
        value = random.choices(wheel_list, k=1)
        combo.extend(value)
    return combo, wheel
