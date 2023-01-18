# 11.3 Методы списков. Часть 1

"""
На вход программе подаются натуральное число n, а затем n строк, каждая на отдельной строке.
Вывести список состоящий из указанных строк.
"""
n = int(input())
lst = []
for el in range(n):
    lst += [input()]
print(lst)


n = int(input())
lst = []
for el in range(n):
    lst.append(input())
print(lst)


"""
Напишите программу, выводящую следующий список (a - z):
['a', 'bb', 'ccc', 'dddd', 'eeeee', 'ffffff', ...]
chr(97) = a
chr(122) = z
"""
abc = []
for el in range(1, 27):
    abc += [chr(96 + el) * el]
print(abc)

# генератор списков
abc = [chr(el) * n for n, el in enumerate(range(97, 123), start=1)]
print(abc)

"""
На вход программе подается натуральное число n, а затем n целых чисел. 
Напишите программу, которая создает из указанных чисел список их кубов.
Input:
    2
    -5
    -2
Output: [-125, -8]
"""
n = int(input())
lst = []
for el in range(n):
    lst += [int(input())]
print(lst)


"""
На вход программе подается натуральное число n. 
Напишите программу, которая создает список состоящий из делителей введенного числа.
Input:  25
Output: [1, 5, 25]
"""
n = int(input())
lst = []
for el in range(1, n + 1):
    if n % el == 0:
        lst += [el]
print(lst)


"""
На вход программе подаются натуральное число n, а затем n целых чисел, каждое на отдельной строке.
Программа должна вывести список, состоящий из сумм соседних чисел.
Input:  
3
1
3
6
4
Output: [4, 9, 10]
"""
n = int(input())
s = [int(input()) for i in range(n)]
for el in range(len(s) - 1):
    s[el] = s[el] + s[el + 1]
s.pop()
print(s)


"""
На вход программе подается натуральное число n и n строк, а затем число k. 
Напишите программу, которая выводит k-ую букву из введенных строк на одной строке без пробелов.
Input: 
    5
    abcdef
    bcdefg
    cdefgh
    d
    ''
    2
Output: bcd
"""
n = int(input())
# s = [[el for el in (input())] for _ in range(n)] # список списков
s = [(input()) for _ in range(n)]  # список строк
k = int(input())
rez = [s[i][k - 1] for i in range(n) if len(s[i]) >= k]
print(''.join(rez))


# решение преподавателя
n = int(input())
s = []
for _ in range(n):
    s.append(input())
k = int(input())
res = ''
for el in s:
    if len(el) >= k:
        res += el[k - 1]
print(res)


"""
На вход программе подается натуральное число  n, а затем n строк. 
Напишите программу, которая создает список из символов всех строк, а затем выводит его.
Примечание. В результирующем списке могут содержаться одинаковые символы.
Input:
    3
    abc
    def
    ghi
Output: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
"""
n = int(input())
s = []
for _ in range(n):
    s.extend(input())
print(s)


# генератор списков
n = int(input())
s = [(input()) for _ in range(n)]
rez = [s[i][k] for i in range(n) for k in range(len(s[i]))]
print(rez)
