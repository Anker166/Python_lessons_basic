# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

import math


class Triangle:

    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3

    @property
    def __a(self):
        return round(math.sqrt((self.x1 - self.x2) ** 2 + (self.y1 - self.y2) ** 2), 2)

    @property
    def __b(self):
        return round(math.sqrt((self.x3 - self.x2) ** 2 + (self.y3 - self.y2) ** 2), 2)

    @property
    def __c(self):
        return round(math.sqrt((self.x3 - self.x1) ** 2 + (self.y3 - self.y1) ** 2), 2)

    def perimeter(self):
        self.__p = round(self.__a + self.__b + self.__c, 2)
        return self.__p

    def area(self):
        self.__s = round(math.sqrt((self.__p / 2) * ((self.__p / 2) - self.__a) * ((self.__p / 2) - self.__b) * ((self.__p / 2) - self.__c)), 2)
        return self.__s

    @property
    def __height_a(self):
        return round((2 * self.__s) / self.__a, 2)

    @property
    def __height_b(self):
        return round((2 * self.__s) / self.__b, 2)

    @property
    def __height_c(self):
        return round((2 * self.__s) / self.__c, 2)

    def heights(self):
        answer = input('Высоту перпендикулярную какой строне считать? (a/b/c)\n').lower()
        if answer == 'a':
            return self.__height_a
        elif answer == 'b':
            return self.__height_b
        elif answer == 'c':
            return self.__height_c


sample = Triangle(1, 1, 4, 4, 6, 2)

print(f'Периметр треугольника: {sample.perimeter()}')
print(f'Площадь треугольника: {sample.area()}')
print(f'Высота треугольника: {sample.heights()}')



# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class IsoscelesTrapezium:

    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
        self.x4 = x4
        self.y4 = y4

    def trapezium_check(self):
        self.__ac = round(math.sqrt((self.x1 - self.x3) ** 2 + (self.y1 - self.y3) ** 2), 2)
        self.__bd = round(math.sqrt((self.x2 - self.x4) ** 2 + (self.y2 - self.y4) ** 2), 2)
        if self.__ac == self.__bd:
            print('Фигура является равнобедренной трапецией')
        else:
            print('Фигура не является равнобедренной трапецией')

    @property
    def __check(self):
        if self.__ac == self.__bd:
            return True
        else:
            return False

    def sides(self):
        if self.__check:
            self.__a = round(math.sqrt((self.x1 - self.x2) ** 2 + (self.y1 - self.y2) ** 2), 2)
            self.__b = round(math.sqrt((self.x2 - self.x3) ** 2 + (self.y2 - self.y3) ** 2), 2)
            self.__c = round(math.sqrt((self.x3 - self.x4) ** 2 + (self.y3 - self.y4) ** 2), 2)
            self.__d = round(math.sqrt((self.x4 - self.x1) ** 2 + (self.y4 - self.y1) ** 2), 2)
            return self.__a, self.__b, self.__c, self.__d
        else:
            return 'Расчет производится только для равнобедренной трапеции'

    def perimeter(self):
        if self.__check:
            self.__p = self.__a + self.__b + self.__c + self.__d
            return self.__p
        else:
            return 'Расчет производится только для равнобедренной трапеции'

    def area(self):
        if self.__check:
            self.__s = ((self.__a + self.__c) / 4) * math.sqrt(4 * (self.__b ** 2) - (self.__a - self.__c) ** 2)
            return self.__s
        else:
            return 'Расчет производится только для равнобедренной трапеции'

sample = IsoscelesTrapezium(1, 1, 3, 5, 5, 5, 7, 1)

sample.trapezium_check()
print(sample.sides())
print(sample.perimeter())
print(sample.area())
