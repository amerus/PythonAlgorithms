'''
В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. Сами минимальный
и максимальный элементы в сумму не включать.
'''

from random import randint

arr = [randint(-100,100) for _ in range(0,10)]
print(arr)

smallest = largest = arr[0]
smallest_pos = largest_pos = 0

for index, item in enumerate(arr):
    if smallest > item:
        smallest = item
        smallest_pos = index
    if largest < item:
        largest = item
        largest_pos = index


start_value = largest_pos if largest_pos < smallest_pos else smallest_pos
end_value = largest_pos if largest_pos > smallest_pos else smallest_pos

print(f"Минимальные и максимальные элементы: {smallest}, {largest}")
print(f"Сумма вложенных элементов: {sum(arr[start_value+1:end_value])}")
