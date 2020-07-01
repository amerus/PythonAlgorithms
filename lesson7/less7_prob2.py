'''
Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на промежутке
[0; 50). Выведите на экран исходный и отсортированный массивы.
'''
from random import randint


def merge_sort(data):
    n = len(data)
    if n == 1:
        return data
    else:
        middle = n // 2
        left = merge_sort(data[:middle])
        right = merge_sort(data[middle:])
    i = j = 0
    result = []
    left_len = len(left)
    right_len = len(right)
    while i < left_len and j < right_len:
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result


size = 20
array = [randint(0, 50) for _ in range(size)]
print(array)
print('*'*45)
print(merge_sort(array))
