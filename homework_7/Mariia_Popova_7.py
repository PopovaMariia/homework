# 1. Написать функцию season, принимающую 1 аргумент — номер месяца (от 1 до 12), и возвращающую время
# года, которому этот месяц принадлежит (зима, весна, лето или осень).

def get_season(number):
    if number.isnumeric():
        number = int(number)
        if any([number == 12, number == 1, number == 2]):
            print('Winter')
        elif 3 <= number <= 5:
            print('Spring')
        elif 6 <= number <= 8:
            print('Summer')
        elif 9 <= number <= 11:
            print('Autumn')
        else:
            print('There is no such month')
    else:
        print('Please use the integer number')

number = input()
get_season(number)

# 2. Реализовать функцию, которая принимает строку и расделитель и возвращает словарь {слово: количество повторений}

def converter(my_str, delimiter):
    import collections
    print(collections.Counter(my_str.split(delimiter)))

my_str = str(input('String'))
delimiter = input('Delimiter')
converter(my_str, delimiter)

# 3. Написать функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения: периметр квадрата,
# площадь квадрата и диагональ квадрата.

def get_rectangle_data(side):
    perimeter = 4 * side
    area = side**2
    diagonal = side**0.5
    print('Perimeter:', round(perimeter), '; area: ', round(area), '; diagonal:', round(diagonal))

side = input()
try:
    side = float(side)
    get_rectangle_data(side)
except ValueError:
    print('Please use number')