# 15.2 Числовая угадайка
""""""

"""
Программа генерирует случайное число в диапазоне от 1 до 100 и
просит пользователя угадать это число.
Если догадка пользователя больше случайного числа,
то программа должна вывести сообщение 'Слишком много, попробуйте еще раз'.
Если догадка меньше случайного числа,
то программа должна вывести сообщение 'Слишком мало, попробуйте еще раз'.
Если пользователь угадывает число,
то программа должна поздравить его и вывести сообщение 'Вы угадали, поздравляем!'.
"""
import random
num = random.randint(1, 100)
while True:
    user_try = int(input('Введите число от 1 до 100: '))
    if user_try < num:
        print('Слишком мало, попробуйте еще раз')
    elif user_try > num:
        print('Слишком много, попробуйте еще раз')
    else:
        print('Вы угадали, поздравляем!')
        break


"""
Тимур загадал число от 1 до n. 
За какое наименьшее количество вопросов (на которые Тимур отвечает "больше" или "меньше") 
Руслан может гарантированно угадать число Тимура?
Input:  8
Output: 3
"""
from math import log2, ceil
n = int(input())
rez = log2(n)
print(ceil(rez))

# Вариант
n = int(input())
count = 0
while n > 1:
    n /= 2
    count += 1
print(count)



"""
Усовершенствованная версия игры "Числовая угадайка":
1 - возможность указания правой границы для случайного выбора числа (от 1 до n)
2 - Проверка введенных данных.
3 - Подсчет попыток, сделанных пользователем. Когда число отгадано, программа должна показать количество попыток.
4 - Возможность генерации нового числа (повторная игра), после того, как пользователь угадал число.
5 - Информация минимального количества попыток угадывания при оптимальной стратегии.
"""


import random
from math import log2, ceil

def is_valid(num, upper_range):
    """
    Проверка корректности введенного пользовательского числа.
    :return: bool
    """
    if str(num).isdigit() and (0 < int(num) <= upper_range):
        return True
    else:
        return False

def is_valid_upper_range(num):
    """
    Проверка корректности задания верхней границы угадываемого диапазона.
    :return: bool
    """
    if str(num).isdigit():
        return True
    else:
        return False


def get_user_num(cnt, upper_range):
    """
    Получение пользовательского числа.
    :return: int
    """
    if cnt > 1:
        print(f"{cnt}-я попытка")

    while True:
        num = input(f"Введите целое число от 1 до {upper_range}: ")
        if is_valid(num, upper_range):
            user_num = int(num)
            return user_num
        else:
            print("Ошибка ввода")


def get_upper_range():
    """
    Получение верхней границы угадываемого диапазона.
    :return: int
    """
    while True:
        num = input("Введите верхний диапазон отгадываемого числа (целое число > 1): ")
        if is_valid_upper_range(num):
            upper_range = int(num)
            return upper_range
        else:
            print("Ошибка ввода")


def guessing_game():
    """
    Игра 'Угадай число'.
    """
    print('Добро пожаловать в числовую угадайку')
    upper_range = get_upper_range()
    game_num = random.randint(1, upper_range)
    cnt = 1

    rez = log2(upper_range)
    print(f"Количество попыток отгадывания при оптимальной стратегии: {ceil(rez)} ")

    while True:
        user_num = get_user_num(cnt, upper_range)
        if user_num < game_num:
            cnt += 1
            print('Ваше число меньше загаданного, попробуйте еще раз.')
        elif user_num > game_num:
            cnt += 1
            print('Ваше число больше загаданного, попробуйте еще раз.')
        else:
            print(f"Вы угадали, поздравляем!\nКоличество попыток: {cnt}")
            break

    qw = input("Хотите сыграть заново?\nВведите 1 для согласия: ")
    if qw == "1":
        guessing_game()


guessing_game()
