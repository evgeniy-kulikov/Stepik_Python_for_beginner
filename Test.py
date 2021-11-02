# import math
# input:
# output:
# Другое решение
# Чужое решение
# Задача 01:
# a, b, c = int(input('')), int(input('')), int(input(''))
# a, b = float(input('')), float(input(''))
# x1, y1, x2, y2 = float(input('')), float(input('')), float(input('')), float(input(''))
# n = float(input())
# n = int(input(''))
# a, b, c = (input('')), (input('')), (input(''))
# x, y, x_1, y_1 = int(input()), int(input()), int(input()), int(input())
# for i in range(10):
# from math import sqrt


user_text = input()
n = 0
while user_text != 'стоп' and user_text != 'хватит' and user_text != 'достаточно':
    n += 1
    user_text = input()
print(n)
