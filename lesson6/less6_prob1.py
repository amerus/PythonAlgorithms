'''
Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. Например, если введено
число 3486, надо вывести 6843.
'''

import sys

# Вывод версий операционной системы и питона
# print(sys.version, sys.platform)
# 3.7.7 (default, May  7 2020, 21:25:33)
# [GCC 7.3.0] linux

# Версия кода 1

number = 3486
# Размер номера (int) 28 байт
print(sys.getsizeof(number))
# size of number 3486 is 28 bytes

reverse = ""
for char in str(number):
    reverse = char + reverse

# размер цифр, обратных по порядку (str) 53 байта
print(sys.getsizeof(reverse))
# size of reversed number presented as string is 53 bytes

# Версия кода 2
# Использование памяти без изменений, так как int переводится в str
print('*' * 50)

number = 3486
print(sys.getsizeof(number))
reverse = str(number)[::-1]
print(sys.getsizeof(reverse))

# Версия кода 3
# Самая эффективная версия. Как number, так и reverse используют 28 байт.
print('*' * 50)

number = 3486
print(sys.getsizeof(number))
reverse = 0
while number > 0:
    remainder = number % 10
    reverse = reverse * 10 + remainder
    number //= 10
print(sys.getsizeof(reverse))
