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

# Задача 07:
# Существуют монеты с номиналами 1, 5, 10, 25.
# Напишите программу, которая определяет какое минимальное количество монет нужно заплатить продавцу.
# input: На вход программе подается одно натуральное число, цена за товар.

coin = 0
residue = 0
price = int(input())

if price >= 25:
    coin = price // 25
    residue = price % 25
    if 10 < residue < 25:
        coin += residue // 10
        residue %= 10
        if 5 < residue < 10:
            coin += residue // 5
        residue %= 5
        if 0 < residue < 5:
            coin += residue

if price < 25:
    coin += price // 10
    residue = price % 10
    if 5 <= residue < 10:
        coin += residue // 5
        residue %= 5
    if 0 < residue < 5:
        coin += residue
print(coin)

