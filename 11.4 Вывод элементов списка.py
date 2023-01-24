# 11.4 Вывод элементов списка

"""
Вывести сумму квадратов элементов списка numbers
"""
numbers = [1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111]
rez = 0
for el in numbers:
    rez += el ** 2
print(rez)

# варианты
rez = sum([el ** 2 for el in numbers])
print(rez)


"""
Значение функции
https://stepik.org/lesson/328948/step/3?unit=312239
На вход программе подается натуральное число n, а затем n целых чисел. 
Напишите программу, которая для каждого введенного числа x выводит значение функции  f(x) = 1^2 + 2x +1 
каждое на отдельной строке
Input:
Output: 
"""

n = int(input())
lst = []
for el in range(n):
    lst.append(int(input()))

for el in lst:
    print(el)

print()

for el in lst:
    rez = el ** 2 + 2 * el + 1
    print(rez)


"""
На вход программе подается натуральное число n, а затем n различных натуральных чисел. 
Напишите программу, которая удаляет наименьшее и наибольшее значение из указанных чисел, 
а затем выводит оставшиеся числа каждое на отдельной строке, не меняя их порядок.
Input:
Output: 
"""
n = int(input())
lst = [int(input()) for _ in range(n)]
lst.remove(max(lst))
lst.remove(min(lst))
print(*lst, sep="\n")

# большое решение
n = int(input())
lst = []
for el in range(n):
    lst.append(int(input()))
num_max = max(lst)
num_min = min(lst)
lst.remove(num_max)
lst.remove(num_min)
for el in lst:
    print(el)

"""
На вход программе подается натуральное число n, а затем n строк. 
Напишите программу, которая выводит только уникальные строки, в том же порядке, в котором они были введены.
Примечание. Все строки состоят из строчных символов.
Input:  5
    first
    second
    first
    third
    second
Output: first
        second
        third
"""
n = int(input())
lst_in = [input() for _ in range(n)]
lst_out = []
for el in lst_in:
    if el not in lst_out:
        lst_out.append(el)
print(*lst_out, sep='\n')

# на каждой итерации проверяем элементы списка до текущего индекса
lst = [input() for _ in range(int(input()))]
for el in range(len(lst)):
    if lst[el] not in lst[:el]:
        print(lst[el])


"""
На вход программе подаются натуральное число n — количество строк, затем сами строки в указанном количестве, 
затем один поисковый запрос.
Примечание. Поиск не должен быть чувствителен к регистру символов.
Input:  5
        Язык Python прекрасен
        C# - отличный язык программирования
        Stepik - отличная платформа
        BEEGEEK FOREVER!
        язык Python появился 20 февраля 1991
        язык
Output:     Язык Python прекрасен
            C# - отличный язык программирования
            язык Python появился 20 февраля 1991

"""
n = int(input())
lst_in = [input() for _ in range(n)]
qs = input().lower()
lst_out = []
for el in lst_in:
    if qs in el.lower():
        lst_out.append(el)
print(*lst_out, sep='\n')

"""
На вход программе подается натуральное число n, затем n строк, 
затем число k — количество поисковых запросов, 
затем k строк — поисковые запросы. 
Напишите программу, которая выводит все введенные строки, в которых встречаются все поисковые запросы.
Примечание. Поиск не должен быть чувствителен к регистру символов.
Input:  5
        Язык Python прекрасен
        C# - отличный язык программирования
        Stepik - отличная платформа
        BEEGEEK FOREVER!
        язык Python появился 20 февраля 1991
        2
        язык
        python
Output:     Язык Python прекрасен
            язык Python появился 20 февраля 1991

"""

n_lst = int(input())
lst = [input() for _ in range(n_lst)]
n_qs = int(input())
lst_qs = [input().lower() for _ in range(n_qs)]
for el in lst:
    cnt = 0
    for k in lst_qs:
        if k in el.lower():
            cnt += 1
    if cnt == len(lst_qs):
        print(el)

# организация дополнительного списка "lst_out"
n_lst = int(input())
lst = [input() for _ in range(n_lst)]
n_qs = int(input())
lst_qs = [input().lower() for _ in range(n_qs)]
lst_out = []

for el in lst:
    cnt = 0
    for k in lst_qs:
        if k in el.lower():
            cnt += 1
    if cnt == len(lst_qs):
        lst_out.append(el)
print(*lst_out, sep='\n')


"""
На вход программе подается натуральное число n, а затем n целых чисел. 
Напишите программу, которая сначала выводит все отрицательные числа, затем нули, а затем все положительные числа, 
каждое на отдельной строке. Числа должны быть выведены в том же порядке, в котором они были введены.
Input:  5
        4
        3
        -2
        -10
        0
Output: -2
        -10
        0
        4
        3
"""
s = [int(input()) for _ in range(int(input()))]
negative = [el for el in s if el < 0]
zero = [el for el in s if el == 0]
positive = [el for el in s if el > 0]
print(*negative, *zero, *positive, sep='\n')
# равносильно следующей записи:
# print(*negative, sep='\n')
# print(*zero, sep='\n')
# print(*positive, sep='\n')
