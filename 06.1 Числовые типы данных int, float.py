# 6.1 Числовые типы данных: int, float
# Для удобного чтения чисел можно использовать символ подчеркивания
# num = 25_000_000   # 25000000
#
# Неявное преобразование.
# Любое целое число (тип int) можно использовать там, где ожидается число с плавающей точкой (тип float),
# поскольку при необходимости Python автоматически преобразует
# целые числа в числа с плавающей точкой.
#
# Явное преобразование.
# Число с плавающей точкой нельзя неявно преобразовать в целое число.
# Для такого преобразования необходимо использовать явное преобразование с помощью команды int().
# преобразование чисел с плавающей точкой в целое производится с округлением в сторону нуля,
# то есть int(1.7) = 1, int(-1.7) = -1

# Задача 1:
# Напишите программу, которая считывает длины двух катетов в прямоугольном треугольнике и выводит его площадь.
# Площадь прямоугольного треугольника S = 1/2 * a * b
# input: На вход программе подаётся два числа с плавающей точкой – длины катетов, каждое на отдельной строке.
# output: Программа должна вывести одно число – площадь треугольника.
a, b = float(input('')), float(input(''))
s = 0.5 * a * b
print(s)

# Задача 2:
# Две старушки идут навстречу друг другу с постоянными скоростями V_1V и V_2 км/ч.
# Определите, через какое время старушки встретятся, если расстояние между ними равно S км.
# input: На вход программе подаются три числа с плавающей точкой S, V_1, V_2 каждое на отдельной строке.
# output: Программа должна вывести одно число в соответствии с условием задачи
s, v1, v2 = float(input('')), float(input('')), float(input(''))
t = s / (v1 + v2)
print(t)

# Задача 3:
# Обратное число (обратная величина) к данному числу x — это число, умножение которого на x даёт единицу.
# Принятая запись: 1/x  (x**-1)
# Напишите программу, которая считывает с клавиатуры одно число и выводит обратное ему.
# Если при этом введённое с клавиатуры число – ноль, то вывести: Обратного числа не существует
# input:  На вход программе подается одно действительное число.
# output: Программа должна вывести действительное число обратное данному, либо текст в соответствии с условием задачи.
a = float(input(''))
if a == 0:
    print('Обратного числа не существует')
else:
    print(1 / a)  # (a ** -1)

# Другое решение
# a == 0 это false
a = float(input())
print(1/a if a else 'Обратного числа не существует')
