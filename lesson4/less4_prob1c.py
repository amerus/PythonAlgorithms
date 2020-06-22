'''
Определить, какое число в массиве встречается чаще всего.
'''
import cProfile
from random import randint

# Using function to hold values in a string instead of array produced by list comprehension
def randomize_me(lin: int):
    l = lin
    array = ""
    for i in range(l):
        value = str(randint(-100, 100))
        array += value + " "
    return array.split(' ')

array = randomize_me(100000000)

def get_counts(arr: list) -> list:
    element_counter = {}

    for item in array:
        if item in element_counter:
            element_counter[item] += 1
        else:
            element_counter[item] = 1

    # with randomize_me function but sort in the end: 100 loops, best of 5: 5.67 nsec per loop
    number, times = sorted(element_counter.items(), key=lambda x: x[1], reverse=True)[0]

    # with randomize_me function but with filter() and max() instead of sorted():
    # 100 loops, best of 5: 6.02 nsec per loop
    # maximum = max(element_counter.values())
    # result = list(filter(lambda x: x[1] == maximum, element_counter.items()))
    # number, times = result[0]

    # with randomize_me function but without sorting in the end: 100 loops, best of 5: 5.64 nsec per loop
    # number = element_counter[max(element_counter, key=element_counter.get)]
    # times = max(element_counter, key=element_counter.get)
    return number, times

number, times = get_counts(array)
# print(f"Номер {number} подсчитывается {times} раз(а) в массиве.")

# cProfile.run('get_counts(array)')
# This cProfile is run with the sorted() way of extracting the counts
#       208 function calls in 12.242 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000   12.242   12.242 <string>:1(<module>)
#      1   12.242   12.242   12.242   12.242 less4_prob1c.py:18(get_counts)
#    202    0.000    0.000    0.000    0.000 less4_prob1c.py:28(<lambda>)
#      1    0.000    0.000   12.242   12.242 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {built-in method builtins.sorted}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#      1    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}
