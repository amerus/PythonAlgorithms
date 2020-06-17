'''
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
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

arr[smallest_pos], arr[largest_pos] = arr[largest_pos], arr[smallest_pos]
print(arr)
