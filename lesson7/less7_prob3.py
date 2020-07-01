'''
Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану. Медианой
называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше медианы,
в другой — не больше медианы.
Примечание: задачу можно решить без сортировки исходного массива. Но если это слишком сложно, используйте метод
сортировки, который не рассматривался на уроках (сортировка слиянием также недопустима).
'''
import random
import statistics


def median_no_sort(arr: list, separation_index):
    pivot = random.choice(arr)

    lows = [el for el in arr if el < pivot]
    highs = [el for el in arr if el > pivot]
    pivots = [el for el in arr if el == pivot]

    n_lows = len(lows)
    n_pivots = len(pivots)

    if separation_index < n_lows:
        return median_no_sort(lows, separation_index)
    elif separation_index < n_lows + n_pivots:
        return pivots[0]
    else:
        return median_no_sort(highs, separation_index - n_lows - n_pivots)


def find_median(arr: list):
    n = len(arr)
    if n % 2 == 1:
        return median_no_sort(arr, n / 2)
    else:
        return 0.5 * (median_no_sort(arr, n / 2 - 1) + median_no_sort(arr, n / 2))


size = 11
for i in range(1000):
    array = [random.randint(0, 100) for _ in range(size)]
    assert statistics.median(array) == find_median(array)
    print('*' * 50)
    print(array)
    print(find_median(array))
    print(sorted(array))
