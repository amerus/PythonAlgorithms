'''
В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой
(оба минимальны), так и различаться.
'''
from random import randint

array = [ randint(0, 100) for _ in range(10) ]
print(array)

first = second = float('inf')

for item in array:
    if item < first:
        second = first
        first = item
    elif first < item < second:
        second = item

print(first, second)
