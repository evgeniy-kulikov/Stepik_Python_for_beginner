"""
https://stepik.org/lesson/534343/step/3?unit=527467
Введите с клавиатуры список с различными значениями (цифры, слова, символы). Необходимо проверить,
есть ли в этом списке два слова подряд и вывести их на экран. Если таких пар нет, то выведите фразу “Мало слов!”.
"""
# test while 12 see 11 like solution
# Привет пока 12 когда 11 что где


# Мое первоначальное решение
def solution_first():
    x = input().split()
    buffer = []
    flag = True
    for el in x:
        if el.isalpha():
            buffer.append(el)
            if len(buffer) == 2:
                print(" ".join(buffer))
                flag = False
        else:
            buffer = []
    if flag:
        print("Мало слов!")

solution_first()


# Мое переделанное решение
def solution_second():
    x = input().split()
    buffer = []
    flag = True
    for el in x:
        if el.isalpha():
            buffer.append(el)
            if len(buffer) == 2:
                print(*buffer)  # распаковка списка [] в строку ""
                flag = False
        else:
            buffer = []
    if flag:
        print("Мало слов!")

solution_second()


# Решения форума
def solution_forum():
    x = input().split()
    flag = True
    for i in range(1, len(x)):
        if x[i - 1].isalpha() and x[i].isalpha():
            print(x[i - 1], x[i], sep=" ")
            flag = False
    if flag:
        print('Мало слов!')

solution_forum()
