# 13 Экзамен
""""""

"""
Напишите функцию draw_triangle(), которая выводит звездный равнобедренный треугольник 
с основанием и высотой равными 15 и 8 соответственно:

Input:  
Output: 
       *
      ***
     *****
    *******
   *********
  ***********
 *************
***************
"""
def draw_triangle():
    k = 7
    s = 1
    for el in range(8):
        print(" " * k + "*" * s)
        k -= 1
        s += 2

draw_triangle()

# вариант преподавателя
def draw_triangle():
    m = 15
    for i in range(1, m + 1, 2):
        print(' ' * ((m - i) // 2) + '*' * i)

draw_triangle()



"""
Интернет магазин осуществляет экспресс доставку для своих товаров 
по цене 1000 рублей за первый товар и 120 рублей за каждый последующий товар.
Напишите функцию get_shipping_cost(quantity), 
которая принимает в качестве аргумента натуральное число quantity – количество товаров в заказе 
и возвращает стоимость доставки.

Input:  print(get_shipping_cost(1))
        print(get_shipping_cost(3))
Output: 1000
        1240
"""

def get_shipping_cost(quantity):
    if quantity == 1:
        return 1000
    else:
        return 1000 + 120 * (quantity - 1)

n = int(input())
print(get_shipping_cost(n))


"""
Напишите функцию compute_binom(n, k), 
которая принимает в качестве аргументов два натуральных числа n и k 
и возвращает значение биномиального коэффициента, равного n! / k! * (n - k)!
где n! и k! это факториалы
Input:  2
        1
Output: 2
"""

from math import factorial
def compute_binom(n, k):
    return int(factorial(n) / (factorial(k) * factorial(n - k)))

n = int(input())
k = int(input())

print(compute_binom(n, k))


"""
Напишите функцию number_to_words(num), 
которая принимает в качестве аргумента натуральное число num и возвращает его словесное описание на русском языке.
Считайте, что число <= num <= 99
Input:  print(number_to_words(85))
Output: восемьдесят пять
"""
d = {
    1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять', 6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять',
    10: 'десять', 11: 'одиннадцать', 12: 'двенадцать', 13: 'тринадцать', 14: 'четырнадцать', 15: 'пятнадцать',
    16: 'шестнадцать',17: 'семнадцать', 18: 'восемнадцать', 19: 'девятнадцать', 20: 'двадцать', 30: 'тридцать',
    40: 'сорок', 50: 'пятьдесят', 60: 'шестьдесят', 70: 'семьдесят', 80: 'восемьдесят', 90: 'девяносто'}

def number_to_words(num):
    if num < 21 or  num % 10 == 0:
        return d[num]
    else:
        return f"{d[num - num % 10]} {d[num % 10]}"

n = int(input())

print(number_to_words(n))




"""
Напишите функцию get_month(language, number), 
которая принимает на вход два аргумента language – язык ru или en и number – номер месяца (от 1 до 12) и 
возвращает название месяца на русском или английском языке.
Input:  print(get_month('ru', 1))
Output: январь

Input:  print(get_month('en', 10))
Output: october
"""
d = {
    'ru': {
        1: 'январь', 2: 'февраль', 3: 'март', 4: 'апрель', 5: 'май', 6: 'июнь', 7: 'июль', 8: 'август',
        9: 'сентябрь', 10: 'октябрь', 11: 'ноябрь', 12: 'декабрь',
    },
    'en': {
        1: 'january', 2: 'february', 3: 'march', 4: 'april', 5: 'may', 6: 'june', 7: 'july', 8: 'august',
        9: 'september', 10: 'october', 11: 'november', 12: 'december',}
    }

def get_month(language, number):
    if language == "ru":
        return d["ru"][number]
    if language == "en":
        return d["en"][number]

lan = input()
num = int(input())

print(get_month(lan, num))


"""
Магическая дата – это дата, когда день, умноженный на месяц, равен числу образованному последними двумя цифрами года.
Напишите функцию, is_magic(date) 
которая принимает в качестве аргумента строковое представление корректой даты и 
возвращает значение True если дата является магической и False в противном случае.
Input:  print(is_magic('10.06.1960'))
Output: True

Input:  print(is_magic('10.06.1961'))
Output: False
"""
def is_magic(date_in):
    d = list(map(int, date_in.split(".")))
    year = d[2] - (d[2] // 100) * 100
    return d[0] * d[1] == year

date = input()

print(is_magic(date))




"""
Панграмма – это фраза, содержащая в себе все буквы алфавита. 
Обычно панграммы используют для презентации шрифтов, чтобы можно было в одной фразе рассмотреть все глифы.
Напишите функцию, is_pangram(text) 
которая принимает в качестве аргумента строку текста на английском языке и возвращает значение True 
если текст является панграммой и False в противном случае.
Input:  print(is_pangram('The jay pig fox zebra and my wolves quack'))
        print(is_pangram('Hello world'))
Output: True
        False
"""

def is_pangram(text):
    s = text.replace(" ", "").lower()
    pangram = ""
    for el in s:
        if el not in pangram:
            pangram += el
    return len(pangram) == 26

text = input()
print(is_pangram(text))


# вариант
def is_pangram(text):
    for i in range(97, 123):
        if not chr(i) in text.lower():
            return False
    return True

text = input()
print(is_pangram(text))
