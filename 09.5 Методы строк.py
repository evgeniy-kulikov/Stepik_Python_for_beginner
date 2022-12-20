# 9.5 Методы строк. Часть 3

# Классификация символов

"""

 isalnum()
Метод isalnum() определяет, состоит ли исходная строка из буквенно-цифровых символов.
Метод возвращает значение True, если исходная строка является непустой и состоит только из буквенно-цифровых символов
и False в противном случае.
s1 = 'abc123'
s1.isalnum()  # True
s2 = 'abc$*123'
s2.isalnum()  # False
s3 = ''
s3.isalnum()  # False


 isalpha()
Метод isalpha() определяет, состоит ли исходная строка из буквенных символов.
Метод возвращает значение True, если исходная строка является непустой и состоит только из буквенных символов
и False в противном случае.
s1 = 'ABCabc'
s1.isdigit()  # True
s2 = 'abc123'
s2.isdigit()  # False
s3 = ''
s3.isdigit()  # False


 islower()
Метод islower() определяет, являются ли все буквенные символы исходной строки строчными (имеют нижний регистр).
Метод возвращает значение True, если все буквенные символы исходной строки являются строчными
и False в противном случае. Все неалфавитные символы игнорируются!
s1 = 'abc'
s1.islower()  # True
s2 = 'abc1$d'
s2.islower()  # True
s3 = 'Abc1$D'
s3.islower()  # False


 isupper()
Метод isupper() определяет, являются ли все буквенные символы исходной строки заглавными (имеют верхний регистр).
Метод возвращает значение True, если все буквенные символы исходной строки являются заглавными
и False в противном случае. Все неалфавитные символы игнорируются!
s1 = 'ABC'
s1.isupper()  # True
s2 = 'ABC1$D'
s2.isupper()  # True
s3 = 'Abc1$D'
s3.isupper()  # False


 isspace()
Метод isspace() определяет, состоит ли исходная строка только из пробельных символов.
Метод возвращает значение True, если строка состоит только из пробельных символов и False в противном случае.
s1 = "    "
s1.isspace()  # True
s2 = 'abc1$d'
s2.isspace()  # False


"""

# Форматирование строк
age = 82
name = 'Ringo'
profession = 'drummer'
txt = 'My name is {}, I am {}, I work as a {}'.format(name, age, profession)
print(txt)  # My name is Ringo, I am 82, I work as a drummer

# f-строки
first_name = 'Ringo'
last_name = 'Star'
age = 82
profession = 'drummer'
affiliation = 'Beatles'
print(f'Hello, {first_name} {last_name}. You are {age}. You are a {profession}. You were a member of {affiliation}')
# Hello, Ringo Star. You are 82. You are a drummer. You were a member of Beatles