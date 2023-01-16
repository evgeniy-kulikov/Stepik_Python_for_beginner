""" 07.2 Цикл for - функция range """

# Функция range(n) с одним параметром - генерирует последовательность чисел от 0 до n-1,
# а цикл for последовательно перебирает эту последовательность.
#
# Перегрузка range(n, m) с двумя параметрами - создает последовательность чисел n, n + 1, n + 2, ..., m - 2, m - 1
#
# Перегрузка range(n, m, k) с 3 параметрами -
# Первый параметр задает старт последовательности,
# второй параметр задает стоп последовательности
# третий параметр – шаг генерации чисел.
# Если шаг генерации является положительным числом, то генерируемая последовательность будет возрастать.
# Мы можем указать отрицательный шаг генерации (третий параметр),
# что приведет к генерированию убывающей последовательности.
#
# Примечания:
# 1) Если величина шага отрицательна и первый параметр меньше второго,
# то функция range() генерирует пустую последовательность.
# Например, вызов функции range(1, 10, -1) приводит к генерации пустой последовательности.
# 2) Функция range() может генерировать только целые числа, включая отрицательные.
# 3) Величина шага не может равняться нулю

# Задача 02:
# Даны два целых числа m и n.
# Напишите программу, которая выводит все числа от m до n включительно в порядке возрастания,
# если m<n, или в порядке убывания в противном случае.
m, n = int(input()), int(input())
if m < n:
    for i in range(m, n + 1):
        print(i)
else:
    for i in range(m, n - 1, -1):
        print(i)

# Задача 03:
# Даны два целых числа m и n (m > n).
# Напишите программу, которая выводит все нечетные числа от m до n включительно в порядке убывания.
# Попробуйте решить задачу двумя способами: с использованием условного оператора if и без него

# с использованием условного оператора if
m, n = int(input()), int(input())
if m % 2 != 0:
    for i in range(m, n - 1, -2):
        print(i)
else:
    for i in range(m - 1, n - 1, -2):
        print(i)

# Без использования оператора if (чужое решение)
"""Если число четное то оно уменьшается на единицу (становиться нечетным). 
Если оно нечетное, то тогда оно не меняется"""
m, n = int(input()), int(input())
mun = ((m - 1) // 2) * 2 + 1
for i in range(mun, n - 1, -2):
    print(i)

# Задача 04:
# Даны два целых числа m и n (m <= n).
# Напишите программу, которая выводит все числа от m до n включительно,
# удовлетворяющие хотя бы одному из условий:
#  - число кратно 17;
#  - число оканчивается на 9;
#  - число кратно 3 и 5 одновременно.
m, n = int(input()), int(input())
for i in range(m, n + 1):
    if (i % 17 == 0) or (i % 10 == 9) or (i % 3 == 0 and i % 5 == 0):
        print(i)

# Задача 05:
# Таблица умножения
num = int(input())
for i in range(1, 11):
    print(f'{num} x {i} = {num * i}')

