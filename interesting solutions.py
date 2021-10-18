# сортировка по убыванию (из трех чисел)
a, b, c = int(input()), int(input()), int(input())
print('start: ', a, b, c)
if a < b:
    b, a = a, b
if c > b:
    c, b = b, c
if c > a:
    c, a = a, c
print('end: ', a, b, c)

# сортировка по возрастанию (из трех чисел)
a, b, c = int(input()), int(input()), int(input())
print('start: ', a, b, c)
if a > b:
    a, b = b, a
if b > c:
    c, b = b, c
if a > b:
    a, b = b, a
print('end: ', a, b, c)
