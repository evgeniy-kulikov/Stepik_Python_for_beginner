# 13.6 Функции с возвратом значения_03
""""""
"""
Функции не ограничены возвратом всего одного значения. 
После инструкции return можно определить много выражений, разделенных запятыми:

return выражение 1, выражение 2, выражение 3 ...
"""

"""
Напишите функцию get_middle_point(x1, y1, x2, y2), 
которая принимает в качестве аргументов координаты концов отрезка 
и возвращает координаты точки являющейся серединой данного отрезка.
Input:  *
Output: *

"""
def get_middle_point(x1, y1, x2, y2):
    x = (x1 + x2) / 2
    y =  (y1 + y2) / 2
    return x, y

x_1, y_1 = int(input()), int(input())
x_2, y_2 = int(input()), int(input())

x, y = get_middle_point(x_1, y_1, x_2, y_2)
print(x, y)


"""
Напишите функцию get_circle(radius), 
которая принимает в качестве аргумента радиус окружности и возвращает два значения: 
длину окружности и площадь круга, ограниченного данной окружностью.
Input:  *
Output: *

"""
from math import pi

def get_circle(radius):
    c = 2 * pi * radius
    s = pi * radius ** 2
    return  c, s

r = float(input())
length, square = get_circle(r)
print(length, square)


"""
Напишите функцию solve(a, b, c), 
которая принимает в качестве аргументов три целых числа a, b, c – коэффициенты квадратного уравнения
ax^2 + bx + c = 0
и возвращает его корни в порядке возрастания.
Прим. Гарантируется, что квадратное уравнение имеет корни.
Input:  1
        -4
        -5
Output: -1.0 5.0
"""
from math import sqrt

def solve(a, b, c):
    discriminant = b ** 2 - (4 * a * c)
    if discriminant > 0:
        root_1 = (-b - sqrt(discriminant)) / (2 * a)
        root_2 = (-b + sqrt(discriminant)) / (2 * a)
        min_root = min(root_1, root_2)
        max_root = max(root_1, root_2)
        return min_root, max_root
    elif discriminant == 0:
        root = -b / (2 * a)
        return root, root


a, b, c = int(input()), int(input()), int(input())
x1, x2 = solve(a, b, c)
print(x1, x2)
