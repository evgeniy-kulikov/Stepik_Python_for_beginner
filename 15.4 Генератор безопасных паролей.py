# 15.4 Генератор безопасных паролей

import random


digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'

# cnt_pwd = input('Укажите количество паролей для генерации: ')
# len_pwd = input('Укажите длину одного пароля: ')
dig_on = input('Включать ли цифры 0123456789? (y/n): ')
upper_on = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? (y/n): ')
lower_on = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? (y/n): ')
symbol_on = input('Включать ли символы !#$%&*+-=?@^_? (y/n): ')
similar_off = input('Исключать ли неоднозначные символы il1Lo0O? (y/n): ')

# chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&*+-=?@^_"

def gen_chars():
    """
    Определение символов для пароля.
    :return: str
    """
    chars = ''
    if dig_on.lower() == 'y':
        chars += digits
    if lower_on.lower() == 'y':
        chars += lowercase_letters
    if upper_on.lower() == 'y':
        chars += uppercase_letters
    if symbol_on.lower() == 'y':
        chars += punctuation
    if similar_off.lower() == 'y':
        for el in 'il1Lo0O':
            chars.replace(el,'')
    return chars


def is_valid(num):
    """
    Проверка корректности введенного пользовательского числа.
    :return: bool
    """
    if str(num).isdigit():
        return True
    else:
        return False


def generate_password(length, chars):
    """
    Создание пароля
    :param length: int
    :param chars: str
    :return:
    """
    password = ""
    for el in range(length):
        password += random.choice(chars)
    return password


def count_pass():
    """
    Количество паролей.
    :return: int
    """
    while True:
        cnt_pwd = input('Укажите количество паролей для генерации: ')
        if is_valid(cnt_pwd):
            cnt_pwd = int(cnt_pwd)
            return cnt_pwd
        else:
            print("Ошибка ввода")


def len_pass():
    """
    Длина пароля.
    :return: int
    """
    while True:
        len_pwd = input('Укажите длину одного пароля: ')
        if is_valid(len_pwd):
            len_pwd = int(len_pwd)
            return len_pwd
        else:
            print("Ошибка ввода")


def create_password_list():
    """
    Создание списка паролей.
    :return:
    """
    cnt_pwd = count_pass()
    len_pwd = len_pass()
    chars = gen_chars()
    for _ in range(cnt_pwd):
        print(generate_password(len_pwd, chars))


create_password_list()
