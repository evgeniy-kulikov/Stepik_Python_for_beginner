""" 07.5.1 цикл while. Обработка цифр числа"""

#  Пусть дано натуральное число n. Тогда:
#   результатом операции n % 10 – является последняя цифра числа;
#   результатом операции n // 10 – является число с удаленной последней цифрой.
#  программа, которая считывает натуральное число (целое положительное) и обрабатывает его цифры.
n = int(input('num: '))
while n != 0:  # пока в числе есть цифры
    last_digit = n % 10  # получить последнюю цифру
    # код обработки последней цифры
    n = n // 10  # удалить последнюю цифру из числа
#  Тело цикла содержит:
# процедуру получения последней цифры last_digit = n % 10;
# код обработки последней цифры;
# процедуру удаления последней цифры из числа n = n // 10.
#  программа, которая определяет есть ли в числе цифра 7.
num = int(input('num: '))
has_seven = False  # сигнальная метка
while num != 0:
    last_digit = num % 10
    if last_digit == 7:
        has_seven = True
        break
    num = num // 10
if has_seven:
    print('YES')
else:
    print('NO')

# Задача 05:
#  Дано натуральное число. Напишите программу, которая меняет порядок цифр числа на обратный.
n = int(input())
num_revers = ''
while n != 0:
    last_digit = n % 10
    n = n // 10
    num_revers += str(last_digit)
print(num_revers)

# другое решение
n = int(input())
while n != 0:  # пока в числе есть цифры
    last_digit = n % 10  # получить последнюю цифру
    print(last_digit, end='')  # печать последней цифры, используем параметр end='' для печати в одну строку
    n = n // 10  # удалить последнюю цифру из числа

# Задача 06
#  Дано натуральное число n, (n≥10). Напишите программу, которая определяет его максимальную и минимальную цифры.
n = int(input())
n_max = 0
n_min = 9
while n != 0:
    last_digit = n % 10
    if last_digit > n_max:
        n_max = last_digit
    if last_digit < n_min:
        n_min = last_digit
    n = n // 10
print(f'Максимальная цифра равна {n_max}')
print(f'Минимальная цифра равна {n_min}')

# другое решение
n = input()
lst = []
for i in range(len(n)):
    lst.append(int(n[i]))
print('Максимальная цифра равна', max(lst))
print('Минимальная цифра равна', min(lst))

# Задача 07
#  Дано натуральное число n. Напишите программу, которая вычисляет:
#  сумму его цифр;
#  количество цифр в нем;
#  произведение его цифр;
#  среднее арифметическое его цифр;
#  его первую цифру;
#  сумму его первой и последней цифры.
n = int(input())
n_sum = 0
n_cnt = 0
n_mlt = 1
n_first = 0
n_end = n % 10
while n > 0:
    last_digit = n % 10
    n_sum += last_digit
    n_cnt += 1
    n_mlt *= last_digit
    n //= 10
    n_first = last_digit
print(n_sum)
print(n_cnt)
print(n_mlt)
print(round((n_sum/n_cnt), 2))
print(n_first)
print(n_first + n_end)

# Задача 08
#  Дано натуральное число n > 9.
#  Напишите программу, которая определяет его вторую (с начала) цифру.
n = int(input())
num = 0
while n > 9:
    last_digit = n % 10
    n //= 10
    num = last_digit
print(num)

#  Задача 09
#  Одинаковые цифры
#  Дано натуральное число. Напишите программу, которая определяет, состоит ли указанное число из одинаковых цифр.
n = int(input())
num = n % 10
cnt_1 = 0  # счетчик одинаковых цифр
cnt_2 = 0  # счетчик итераций цикла
while n > 0:
    last_digit = n % 10
    if num == last_digit:
        cnt_1 += 1
    n //= 10
    cnt_2 += 1
if cnt_1 == cnt_2:
    print('YES')
else:
    print('NO')

# другое решение (через список)
#  преобразуем строку в список
n = list(map(int, list(input())))
print("YES" if max(n) == min(n) else "NO")


#  Задача 10
#  Дано натуральное число. Напишите программу, которая определяет,
#  является ли последовательность его цифр при просмотре справа налево упорядоченной по неубыванию.
#  Например 5321 -> YES,   7820 -> NO

n = int(input())
num = n % 10
flag = True
while n > 0:
    last_digit = n % 10
    if num <= last_digit:
        flag = True
    else:
        flag = False
        break
    num = last_digit
    n //= 10
if flag:
    print('YES')
else:
    print('NO')
