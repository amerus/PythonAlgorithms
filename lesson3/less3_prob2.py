'''
Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив со значениями
8, 3, 15, 6, 4, 2, второй массив надо заполнить значениями 0, 3, 4, 5 (помните, что индексация начинается с нуля),
т. к. именно в этих позициях первого массива стоят четные числа.
'''

from random import randint

array = [randint(0, 10) for _ in range(10)]
print(array)

even_positions = []

for index, item in enumerate(array):
    if item % 2 == 0:
        even_positions.append(index)

print(even_positions)
