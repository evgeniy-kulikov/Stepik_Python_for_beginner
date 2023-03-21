# 15.5 Шифр Цезаря
""""""

# Шифр Цезаря (Начальный вариант)

# Задаем четыре вопроса пользователю: шифр-дешифр, язык, шаг, текст.
whats_direction = input('Направление (введите 1 / 2): 1-шифровать / 2-дешифровать?\n').lower()
while whats_direction != '1' and whats_direction != '2':
    whats_direction = input('Ошибка ввода. Введите 1 или 2\n').lower()

whats_language = input('Язык текста (введите ru / en): ru-русский / en-английский?\n').lower()
while whats_language != 'ru' and whats_language != 'en':
    whats_language = input('Ошибка ввода. Введите ru / en\n').lower()

whats_step = input('Размер сдвига. Введите число.\n')
while whats_step.isdigit() != True:
    whats_step = input('Ошибка ввода. Введите число.\n')

whats_text = input('Введите текст для преобразования\n')
while whats_text.isspace() == True or whats_text == "":
    whats_text = input('Ошибка ввода. Введите текст. \n')


# Объявляем функцию с четырьмя аргументами – соответственно четырем вопросам.
def caesar(direction, language, step, text):
    # Четыре словаря под русские и английские символы, большие и маленькие.
    upper_eng_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower_eng_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    upper_rus_alphabet = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    lower_rus_alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'

    # Задаем локальные переменные: длину алфавита и значения словарей.
    if language == 'ru':
        alphas = 32
        low_alphabet = lower_rus_alphabet
        upp_alphabet = upper_rus_alphabet
    if language == 'en':
        alphas = 26
        low_alphabet = lower_eng_alphabet
        upp_alphabet = upper_eng_alphabet

    for el in range(len(text)):
        if text[el].isalpha():
            # Находим индекс символа в словаре upp_alphabet либо low_alphabet.
            if text[el] == text[el].lower():
                place = low_alphabet.index(text[el])
            if text[el] == text[el].upper():
                place = upp_alphabet.index(text[el])

            if direction == '2':  # дешифровать
                # Индекс для измененного символа.
                index = (place - int(step)) % alphas

            if direction == '1':  # шифровать
                # Индекс для измененного символа.
                index = (place + int(step)) % alphas

            # Выводим измененный символ.
            if text[el] == text[el].lower():
                print(low_alphabet[index], end='')
            if text[el] == text[el].upper():
                print(upp_alphabet[index], end='')

                # Если text[el] не является буквой:
        else:
            # Делаем print этого символа без изменений.
            print(text[el], end='')


"""   *   *   *   Task   *   *   *   """

"""
Текст "Hawnj pk swhg xabkna ukq nqj." 
был получен в результате шифрования алгоритмом Цезаря с сдвигом вправо на n символов. 
Расшифруйте данный текст.
Считайте, что  0 <= n <= 25

Input:  Hawnj pk swhg xabkna ukq nqj.
Output: Learn to walk before you run.
"""

text_in = "Hawnj pk swhg xabkna ukq nqj."
for k in range(26):
    for el in text_in:
        if el in ',.?! ':
            print(el, end='')
        elif 65 <= ord(el) <= 90:
            print(chr((ord(el) - k - 65) % 26 + 65), end='')
        elif 97 <= ord(el) <= 122:
            print(chr((ord(el) - k - 97) % 26 + 97), end='')
    print()

"""
На вход программе подается строка текста на английском языке, в которой нужно зашифровать все слова. 
Каждое слово строки следует зашифровать с помощью шифра Цезаря. Циклический сдвиг - длина этого слова (только буквы). 
Строчные буквы при этом остаются строчными, а прописные – прописными.

Input:  Day, mice. "Year" is a mistake!
Output: Gdb, qmgi. "Ciev" ku b tpzahrl!

Input:  my name is Python!
Output: oa reqi ku Veznut!
"""
def caesar(step, text):
    upp_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    low_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    txt_out = ""
    alphas = 26

    for el in range(len(text)):
        if text[el].isalpha():
            if text[el] == text[el].lower():
                place = low_alphabet.index(text[el])
            if text[el] == text[el].upper():
                place = upp_alphabet.index(text[el])

            index = (place + int(step)) % alphas

            if text[el] == text[el].lower():
                txt_out += low_alphabet[index]
            if text[el] == text[el].upper():
                txt_out += upp_alphabet[index]
        else:
            txt_out += text[el]
    return txt_out


text_in = input()
text = text_in.split()
text_out = ""

for el in text:
    word_step = 0
    for k in el:
        if k.isalpha():
            word_step += 1
    text_out += caesar(word_step, el) + " "
print(text_out[:-1])

# Вариант 1
low_alphabet = 'abcdefghijklmnopqrstuvwxyz'
up_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
text_in = input().split()
text_out = ''

for el in text_in:
    step = len([i for i in el if i.isalpha()])
    for k in el:
        if k in up_alphabet:
            text_out += up_alphabet[(up_alphabet.find(k) + step) % 26]
        elif k in low_alphabet:
            text_out += low_alphabet[(low_alphabet.find(k) + step) % 26]
        else:
            text_out += k
    text_out += ' '

print(text_out[:-1])


# Вариант 2
low_alphabet = [chr(x) for x in range(ord('a'), ord('z') + 1)]
# ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
# 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
text_out = ""
text_in = input().split()

for el in text_in:
    # step = len(''.join(filter(str.isalpha, el)))
    step = len(list(filter(str.isalpha, el)))
    for k in el:
        if k.isupper():
            text_out += low_alphabet[(step + low_alphabet.index(k.lower())) % 26].upper()
        elif k.islower():
            text_out += low_alphabet[(step + low_alphabet.index(k)) % 26]
        else:
            text_out += k
    text_out += ' '
print(text_out)
