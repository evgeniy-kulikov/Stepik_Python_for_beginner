# 11.1 Введение в списки

"""
Напишите программу, которая выводит список [1, 2, 3, ..., n].
"""

# генератор списков
n = int(input())
print([i for i in range(1, n + 1)])

# list()
n = int(input())
print(list(range(1, n + 1)))

"""
На вход программе подается одно число  n ≤26 
Напишите программу, которая выводит список, 
состоящий из n букв английского алфавита ['a', 'b', 'c', ...] в нижнем регистре.
"""
n = int(input())
print([chr(i) for i in range(97, n + 97)])

