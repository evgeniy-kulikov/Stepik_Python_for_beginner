# 11.7 Списочные выражения

"""
Дополните приведенный код, используя списочное выражение так,
чтобы получить новый список, содержащий строки исходного списка с удаленным первым символом.
"""
keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue',
            'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if',
            'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
new_keywords = [el[1:] for el in keywords]
print(new_keywords)


"""
Дополните приведенный код, используя списочное выражение, так 
чтобы получить новый список, содержащий длины строк исходного списка.
"""
keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def',
            'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import',
            'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
lengths = [len(el) for el in keywords]
print(lengths)


"""
Дополните приведенный код списочным выражением, чтобы получить новый список, 
содержащий только слова длиной не менее пяти символов (включительно)
"""
keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def',
            'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import',
            'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
new_keywords = [el for el in keywords if len(el) > 4]
print(new_keywords)


"""
Дополните приведенный код, используя списочное выражение, так 
чтобы получить список всех чисел палиндромов от 100 до 1000 (зеркальные числа)
"""
palindromes = [el for el in range(100, 1000) if str(el)[0] == str(el)[-1]]
print(palindromes)

# вариант
palindromes = [i for i in range(100, 1000) if i % 10 == i // 100]
print(palindromes)


"""
На вход программе подается натуральное число n. 
Напишите программу, использующую списочное выражение, которая создает список содержащий квадраты чисел от 1 до n, 
а затем выводит его элементы построчно, то есть каждый на отдельной строке.
Примечание. Для вывода элементов списка используйте цикл for
Input:  5
Output: 1
        4
        9
        16
        25
"""
lst = [el ** 2 for el in range(1, int(input()) + 1)]
print(*lst, sep='\n')


"""
На вход программе подается строка текста, содержащая целые числа. 
Напишите программу, использующую списочное выражение, 
которая выведет кубы указанных чисел также на одной строке.
Примечание 1. Для вывода элементов списка используйте цикл for
Примечание 2. Используйте метод split()
Input:  2 4 3
Output: 8 64 27
"""
s = list(map(int, input().split()))
s = [el ** 3 for el in s]
print(*s)


"""
На вход программе подается строка текста, содержащая слова. 
Напишите программу, которая выводит слова введенной строки в столбик.
Input:  Умей ценить того кто без тебя не может
Output: Умей
        ценить
        того
        кто
        без
        тебя
        не
        может
"""
s = list(map(str, input().split()))
print(*s, sep='\n')

# короче
s = [print(el) for el in input().split()]


"""
На вход программе подается строка текста. 
Напишите программу, использующую списочное выражение, 
которая выводит все цифровые символы данной строки.
Input:  123Python awesome!56
Output: 12356
"""
s = [el for el in input() if el.isdigit()]
print(*s, sep='')

# короче
s = [print(el, end='') for el in input() if el.isdigit()]


"""
На вход программе подается строка текста, содержащая целые числа. 
Напишите программу, использующую списочное выражение, 
которая выведет квадраты четных чисел, которые не оканчиваются на цифру 4
Input:  1 2 3 4 5 6 7 8 9
Output: 16 36
"""
s = list(map(int, input().split()))
s = [el ** 2 for el in s if el % 2 == 0 and (el ** 2) % 10 != 4]
print(*s)

# одна строка
[print(el ** 2, end=' ') for el in list(map(int, input().split())) if el % 2 == 0 and el ** 2 % 10 != 4]
