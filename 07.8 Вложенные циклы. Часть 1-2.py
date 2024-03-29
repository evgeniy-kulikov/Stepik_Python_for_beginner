# Задача 02
# Что покажет приведенный ниже фрагмент кода?

for i in range(1, 4):
    for j in range(3, 5):
        print(i + j, end='')
# 455667

# Задача 03
# Что покажет приведенный ниже фрагмент кода?

counter = 0
for i in range(99, 102):
    temp = i
    while temp > 0:
        counter += 1
        temp //= 10
print(counter)
# 8

# Задача 04
# Дано натуральное число n , (n ≤ 9 ). Напишите программу, которая печатает таблицу
# размером n × 3 состоящую из данного числа (числа отделены одним пробелом).
n = int(input())
for i in range(n):
    for j in range(3):
        print(n, end=' ')
    print()
# >>> 4
# 4 4 4
# 4 4 4
# 4 4 4
# 4 4 4

# другое рещение (без вложенного цикла)
n = int(input())
for i in range(1, n+1):
    print(f'{n} ' * 3)

# Задача 05
# Дано натуральное число n , (n ≤ 9 ). Напишите программу, которая печатает таблицу
# размером n × 5, где в i-ой строке указано число i (числа отделены одним пробелом).

n = int(input())
for i in range(1, n + 1):
    print(f'{i} ' * 5)

# >>> 4
# 1 1 1 1 1
# 2 2 2 2 2
# 3 3 3 3 3
# 4 4 4 4 4

# другое рещение (вложенный цикл)
n = int(input())
for i in range(1, n + 1):
    for j in range(5):
        print(i, end=' ')
    print()

# Задача 06
# Дано натуральное число  (n≤ 9). Напишите программу, которая печатает
# таблицу сложения для всех чисел от 1 до n.

n = int(input())
for i in range(1, n + 1):  # от 1 до "n" включительно
    for k in range(1, 10):
        print(f'{i} + {k} = {i + k}')
    print()  # для разрыва между столбцами

# >>> 2

# 1 + 1 = 2
# 1 + 2 = 3
# 1 + 3 = 4
# 1 + 4 = 5
# 1 + 5 = 6
# 1 + 6 = 7
# 1 + 7 = 8
# 1 + 8 = 9
# 1 + 9 = 10
#
# 2 + 1 = 3
# 2 + 2 = 4
# 2 + 3 = 5
# 2 + 4 = 6
# 2 + 5 = 7
# 2 + 6 = 8
# 2 + 7 = 9
# 2 + 8 = 10
# 2 + 9 = 11

# Задача 07
# Дано нечетное натуральное число n.
# Напишите программу, которая печатает равнобедренный звездный треугольник
# с основанием, равным n

n = int(input())
for i in range(1, n + 1):
    if i <= int(n / 2 + 1):
        print('*' * i, sep='')
        continue
    for k in range(1):
        print('*' * (n - i + 1), sep='')
# >>> 5
# *
# **
# ***
# **
# *

# Задача 08
# Дано натуральное число n. Напишите программу, которая печатает численный треугольник.

n = int(input())
for i in range(1, n + 1):
    print(str(i) * i)

# решение через вложенные циклы
n = int(input())
for i in range(1, n+1):
    for j in range(i):
        print(i, end='')
    print()
# 1
# 22
# 333
# 4444
# 55555
# ...
