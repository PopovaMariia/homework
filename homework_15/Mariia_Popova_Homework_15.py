"""
Реализовать класс фигуры. На основе фигуры реализовать класс треугольника, квадрата и прямоугольника
с методами подсчета площади и периметра. Методы должны возвращать значение, а не принтить (это важно)
"""


class Square:
    def __init__(self, side_1):
        self.side_1 = side_1

    def perimeter(self):
        return self.side_1 * 4

    def area(self):
        return self.side_1 ** 2


class Triangle(Square):
    def __init__(self, side_1, side_2, side_3):
        super().__init__(side_1)
        self.side_2 = side_2
        self.side_3 = side_3

    def perimeter(self):
        return self.side_1 + self.side_2 + self.side_3

    def area(self):
        p = ((self.perimeter()) / 2)
        return (p * (p - self.side_1) * (p - self.side_2) * (p - self.side_3)) ** 0.5


class Rectangle(Square):
    def __init__(self, side_1, side_2):
        super().__init__(side_1)
        self.side_2 = side_2

    def perimeter(self):
        return (self.side_1 + self.side_2) * 2

    def area(self):
        return self.side_1 * self.side_2


if __name__ == '__main__':
    var = Rectangle(3, 5)
    print(var.perimeter())
    print(var.area())
