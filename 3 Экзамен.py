# правильные строки
print("Told you not to worry", "But maybe that's a lie", sep=' :) ')
print("Honey, what's your hurry", end='?')
print("The world's a little blurry", "Or maybe it's my eyes", end='!!!', sep=' :) ')

# Напишите программу, которая считывает два целых числа a и b и выводит на экран квадрат суммы (a+b)^2
# и сумму квадратов a^2+b^2a  этих чисел.
a, b = int(input()), int(input())
sqw = (a + b)**2
sym = a**2 + b**2
print(f'Квадрат суммы {a} и {b} равен {sqw}')
print(f'Сумма квадратов {a} и {b} равна {sym}')

# Программа должна получить число  в виде ( n nn nnn ) и выдать сумму его составляющих чисел n + nn + nnn
# пояснение:
# 1 + 11 + 111 = 123
# 2 + 22 + 222 = 246
# . . . . .
# 8 + 88 + 888 = 984
# 9 + 99 + 999 = 1107
n1 = int(input(''))
n2 = n1*10 + n1
n3 = n1*100 + n2
print(n1 + n2 + n3)
