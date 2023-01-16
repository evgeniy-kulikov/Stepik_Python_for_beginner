# Общий алгоритм получения цифр n-значного числа
n, num = 4, 1234
digit1 = (num % 10 ** n) // 10**(n-1)      # num // 1000
digit2 = (num % 10 ** (n-1)) // 10**(n-2)  # (num % 1000) // 100
digit3 = (num % 10 ** (n-2)) // 10**(n-3)  # (num % 100) // 10
digit4 = (num % 10 ** (n-3)) // 10**(n-4)  # num % 10
print(digit1, digit2, digit3, digit4, sep='')

print(True)  # True
print(False)  # False
print(True + True)  # 2
print(False + False)  # 0
print(False + True)  # 1
print(True * True)  # 1
print(False * False)  # 0
print(False * True)  # 0
print(['a', 'b', 'c'][0])  # a
st = ['a', 'b', 'c']
print(st.index('b'))  # 1
print(st[2])  # c

# печать в одну строку в теле цикла
n = int(input())
for i in range(n):
    print(n, end=' ')

# преобразовать список my_list в строку my_str
my_list = []
my_str = ''.join(str(i) for i in my_list)

# Тернарный оператор
s = [1, 3, 8, 9]
print((False, True)[1 in s])
