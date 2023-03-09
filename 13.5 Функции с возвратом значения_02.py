# 13.5 Функции с возвратом значения_02
""""""

""" Возвращение булевых значений """
"""
Напишем программу, которая просит пользователя ввести число, и определяет четное оно или нечетное.
"""
number = int(input())
if number % 2 == 0:
    print('Это число четное. ')
else:
    print('Это число нечетное.')


# Переделаем этот код в функцию с возвратом значения
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

number = int(input())
if is_even(number):
    print('Это число четное. ')
else:
    print('Это число нечетное.')


""" Использование булевых функций для валидации входных данных """
""" 
Пример программы, предлагающей пользователю ввести номер модели изделия, 
где возможны только значения 100, 200 и 300
"""
model = int(input())

while model != 100 and model != 200 and model != 300:
    print('Допустимыми номерами моделей являются 100, 200 и 300.')
    model = int(input())


# Переделаем этот код в функцию с возвратом значения
def is_invalid(model):
    if model != 100 and model != 200 and model != 300:
        return True
    else:
        return False

while is_invalid(model):
    print('Допустимыми номерами моделей являются 100, 200 и 300.')
    model = int(input())

"""
Создание функций, реализующих такую простую логику — не всегда оптимальное решение, 
так как увеличивает размер кода и ведет к затратам времени на вызов функции 
и возврат обратно результата, что может сказаться на производительности программы.
"""


"""   *   *   *   *    З А Д А Ч И     *   *   *   *   """

"""
Напишите функцию is_valid_triangle(a, b, c), 
которая принимает в качестве аргументов три натуральных числа, и 
возвращает значение True если существует невырожденный треугольник со сторонами a, b, c
и False в противном случае
Input:  3
        4
        5
Output: True
"""
def is_valid_triangle(a, b, c):
    if (a < (b + c)) and (b < (a + c)) and (c < (a + b)):
        return True
    else:
        return False

a, b, c = int(input()), int(input()), int(input())
print(is_valid_triangle(a, b, c))


"""
Напишите функцию is_prime(num), которая принимает в качестве аргумента натуральное число 
и возвращает значение True если число является простым и False в противном случае.
Input:  17
Output: True
"""
def is_prime(num):
    if num == 1:
        return False
    for k in range(2, num):
        if num % k == 0:
            return False
    return True

n = int(input())
print(is_prime(n))


"""
Напишите функцию get_next_prime(num), 
которая принимает в качестве аргумента натуральное число num 
и возвращает первое простое число большее числа num
Input:  9
Output: 11
"""
def is_prime(num):
    # if num == 1:
    #     return False
    for k in range(2, num):
        if num % k == 0:
            return False
    return True


def get_next_prime(n):
    n += 1
    while not is_prime(n):
        n += 1
    return  n

n = int(input())
print(get_next_prime(n))



"""
Напишите функцию is_password_good(password), 
которая принимает в качестве аргумента строковое значение пароля password и 
возвращает значение True если пароль является надежным и False в противном случае.
Пароль является надежным если:
его длина не менее 8 символов; 
он содержит как минимум одну заглавную букву (верхний регистр); 
он содержит как минимум одну строчную букву (нижний регистр);
он содержит хотя бы одну цифру.
Input:  aabbCC11OP
Output: True
"""
def is_password_good(password):
    if len(password) > 7:
        if len([_ for _ in password if _ in list('1234567890')]) > 0:
            if len([_ for _ in password if _.isupper()]) > 0:
                if len([_ for _ in password if _.islower()]) > 0:
                    return True
    return False

txt = input()
print(is_password_good(txt))


# Возможное решение задачи:
def is_password_good(password):
    if len(password) < 8:
        return False
    flag1 = False
    flag2 = False
    flag3 = False
    for c in password:
        if c.isupper():
            flag1 = True
        elif c.islower():
            flag2 = True
        elif c.isdigit():
            flag3 = True
    return flag1 and flag2 and flag3


txt = input()
print(is_password_good(txt))


"""
Напишите функцию is_one_away(word1, word2), 
которая принимает в качестве аргументов два слова word1 и word2 и 
возвращает значение True если слова имеют одинаковую длину и 
отличаются ровно в 1 символе и False в противном случае.
Input:  bike
        hike
Output: True
"""
def is_one_away(word1, word2):
    if len(word1) == len(word2):
        cnt = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                cnt += 1
        if cnt == 1:
            return True
    return False

txt1, txt2 = input(), input()
print(is_one_away(txt1, txt2))


# Вариант через zip:
def is_one_away(word1, word2):
    if len(word1) == len(word2):
        lst = [i == k for i, k in zip(word1, word2)]
        if lst.count(False) == 1:
            return True
    return False

txt1, txt2 = input(), input()
print(is_one_away(txt1, txt2))


"""
Напишите функцию is_palindrome(text), 
которая принимает в качестве аргумента строку text и 
возвращает значение True если указанный текст является палиндромом и False в противном случае.
Примечание 1. Палиндром – это строка, которая читается одинаково в обоих направлениях
Примечание 2. При проверке считайте большие и маленькие буквы одинаковыми, 
              а также игнорируйте пробелы, а также символы , . ! ? -
Input:  Standart - smallest, sell Amstrad nats
Output: True
"""
def is_palindrome(text):
    s = text.lower()
    for el in s:
        if el in ',.!?-':
            s = s.replace(el, '')
    w = s.split()
    w = ''.join(w)
    return w == w[::-1]

txt = input()
print(is_palindrome(txt))


# Возможное решение задачи:
def is_palindrome(text):
    symbols = [' ', ',', '.', '!', '?', '-']
    for el in symbols:
        text = text.replace(el, '')
    text = text.lower()
    return text == text[::-1]

txt = input()
print(is_palindrome(txt))



"""
Пароль имеет вид a:b:c, где a, b и c – натуральные числа, где:
число a – должно быть палиндромом;
число b – должно быть простым;
число c – должно быть четным.
Напишите функцию is_valid_password(password), 
которая принимает в качестве аргумента строковое значение пароля password и 
возвращает значение True если пароль является действительным паролем и 
False в противном случае.
Input:  1221:101:22
Output: True
"""

def is_simple(num):
    for el in range(2, num):
        if num % el == 0:
            return False
    return True

def is_valid_password(password):
    s = password.split(":")
    if len(s) == 3:
        if s[0] == s[0][::-1]:
            if int(s[2]) % 2 == 0:
                if is_simple(int(s[1])):
                    return True
    return False

psw = input()
print(is_valid_password(psw))



"""
Напишите функцию is_correct_bracket(text), 
которая принимает в качестве аргумента непустую строку text, 
состоящую из символов "(" и ")" и возвращает значение 
True если поступившая на вход строка является ПРАВИЛЬНОЙ скобочной последовательностью и 
False в противном случае.
Input:  ((()))
Output: True

Input:  ())(()
Output: False
"""

def is_correct_bracket(text):
    cnt_in = 0
    cnt_out = 0
    for el in text:
        if el == "(":
            cnt_in += 1
        if el == ")":
            cnt_out += 1
        if cnt_in - cnt_out == -1:
            return False
    return cnt_in == cnt_out
    # if cnt_in != cnt_out:
    #     return False
    # return True

txt = input()
print(is_correct_bracket(txt))


"""
Напишите функцию convert_to_python_case(text), 
которая принимает в качестве аргумента строку в «верблюжьем регистре» и 
преобразует его в «змеиный регистр».
Input:  ThisIsCamelCased
Output: this_is_camel_cased

"""
def convert_to_python_case(text):
    s = [el for el in text]
    upper = [el for el in text if el.isupper()]
    for el in s:
        if el in upper:
            s[s.index(el)] = "_" + el.lower()
            upper.remove(el)
    s = "".join(s)
    return s[1:]

txt = input()
print(convert_to_python_case(txt))



# Возможное решение задачи:
def convert_to_python_case(text):
    s = ''
    for el in text:
        if el.isupper():
            s += '_' + el.lower()
        else:
            s += el
    return s[1:]

txt = input()
print(convert_to_python_case(txt))
