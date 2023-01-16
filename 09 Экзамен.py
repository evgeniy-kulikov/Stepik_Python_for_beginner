"""
Напишите программу, которая удаляет из нее все символы с индексами кратными 3, то есть символы с индексами 0, 3, 6, ....
Input: Python
Output: yton
"""

# s = 'Python'
s = input()
s_new = ''
for i in range(len(s)):
    if i % 3 != 0:
        s_new += s[i]
print(s_new)


"""
На вход программе подается строка текста. Напишите программу, которая заменяет все вхождения цифры 1 на слово «one».
Input: 1231
Output: one23one
"""

# s = '1231'
s = input()
s_new = ''
for i in range(len(s)):
    if s[i] == '1':
        s_new += 'one'
    else:
        s_new += s[i]
print(s_new)


"""
На вход программе подается строка текста. Напишите программу, которая удаляет все вхождения символа «@».
Input: 123@1@@34
Output: 123134

Input: @@
Output: ''
"""
# s = '123@1@@34'
s = input()
print(s.replace('@', ''))



"""
На вход программе подается строка текста.
Напишите программу, которая выводит индекс второго вхождения буквы «f».
Если буква «f» встречается только один раз, выведите число -1,
а если не встречается ни разу, выведите число -2.
Input: affective
Output: 2

Input: father
Output: -1

Input: python
Output: -2
"""
# s = 'affective'
s = input()
if s.count('f') == 1:
    print('-1')
elif s.count('f') == 0:
    print('-2')
else:
    print(s.find('f', s.find('f') + 1))

"""
На вход программе подается строка текста в которой буква «h» встречается как минимум два раза.
Напишите программу, которая возвращает исходную строку и переворачивает последовательность символов,
заключенную между первым и последним вхождением буквы «h».

Input: abch12345h
Output: abch54321h

Input: qwertyhasdfghzxcvb
Output: qwertyhgfdsahzxcvb

"""
s = input()
h_in = s.find('h')
h_out = s.rfind('h')
s_cut = s[h_in:h_out + 1]  # включая "h" на концах
answer = s[:h_in] + s_cut[::-1] + s[h_out + 1:]
print(answer)
