# 11.6 Методы списков. Часть 2

"""
Для строки
numbers = [8, 9, 10, 11]

Напишите код, чтобы он:
Заменил второй элемент списка на 17;
Добавил числа 4, 5 и 6 в конец списка;
Удалил первый элемент списка;
Удвоил список;
Вставил число 25 по индексу 3;
Вывел список, с помощью функции print()
"""
numbers = [8, 9, 10, 11]
numbers[1] = 17
numbers += [4, 5, 6]  # numbers.extend([4, 5, 6])
numbers.remove(8)  # del numbers[0]
numbers += numbers  # numbers *= 2
numbers.insert(3, 25)
print(numbers)


"""
На вход программе подается строка текста, содержащая различные натуральные числа, разделенные символом пробела. 
Из данной строки формируется список чисел. Напишите программу, 
которая меняет местами минимальный и максимальный элемент этого списка.
Input:  3 4 5 2 1
Output: 3 4 1 2 5
"""
s = list(map(int, input().split()))
i_min = s.index(min(s))
i_max = s.index(max(s))
s[i_min], s[i_max] = s[i_max], s[i_min]
print(*s)


"""
На вход программе подается строка, содержащая английский текст. 
Напишите программу, которая подсчитывает общее количество артиклей: 'a', 'an', 'the'
Input:  William Shakespeare was born in the town of Stratford, England, in the year 1564. When he was a young man, Shakespeare moved to the city of London, where he began writing plays. His plays were soon very successful, and were enjoyed both by the common people of London and also by the rich and famous. In addition to his plays, Shakespeare wrote many short poems and a few longer poems. Like his plays, these poems are still famous today.
Output: 7
"""
s = list(input().lower().split())
a = s.count('a')
an = s.count('an')
the = s.count('the')
print(f"Общее количество артиклей: {a + an + the}")

# вариант
s = list(input().lower().split())
cnt = 0
for i in ['a', 'an', 'the']:
    cnt += s.count(i)
print(f"Общее количество артиклей: {cnt}")

"""
На первой строке вводится символ решётки и сразу же натуральное число n — количество строк в программе, 
не считая первой. Далее следует n строк кода.
Убрать из каждой строчки кода "#" и сам комментарий, а так же пробел между "#" и строкой кода)
Input:  
#2
if password == "hoover":
    print("Здравствуйте, рыцарь", name)         #долой Макнамару

Output:
if password == "hoover":
    print("Здравствуйте, рыцарь", name) 
"""
# список для тестирования
# s = ['print("Введите своё имя")',
#      'name = input()',
#      'print("Введите пароль, если имеется")    # ахахахах вам не поймать меня',
#      'password = input()',
#      'if password == "hoover":',
#      '     print("Здравствуйте, рыцарь", name)         #долой Макнамару',
#      'elif password == "noncr":',
#      '     print("Здравствуйте, паладин", name)',
#      'elif password == "gelios":',
#      '     print("Здравствуйте, старейшина", name)          #Элайджа вперёд',
#      'else:'
#      '     print("Здравствуйте, послушник", name)']

n = int(input()[1:])
lst = []
for _ in range(n):
    lst.append(input())
for el in lst:
    el = el.split("#")
    print(el[0].rstrip())

# вариант преподавателя (без организации списка)
n = input()
for _ in range(int(n[1:])):
    s = input()
    if '#' in s:
        s = s[:s.find('#')]
    print(s.rstrip())


"""
На вход программе подается строка текста, содержащая целые числа. 
Из данной строки формируется список чисел. 
Напишите программу, которая сортирует и выводит данный список сначала по возрастанию, а затем по убыванию. 
Input:  4 5 1 2 3 8
Output: 1 2 3 4 5 8
        8 5 4 3 2 1
"""
lst = list(map(int, input().split()))
lst.sort()
print(*lst)
lst.sort(reverse=True)
print(*lst)
