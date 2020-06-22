'''
Определить, какое число в массиве встречается чаще всего.
'''

import cProfile
import numpy as np

# Using numpy random number generator instead of random.randint:
# 100 loops, best of 5: 6.23 nsec per loop

array = np.random.randint(-100, 100, 100000000)


def get_counts(arr: list) -> list:
    element_counter = {}

    for item in array:
        if item in element_counter:
            element_counter[item] += 1
        else:
            element_counter[item] = 1

    number, times = sorted(element_counter.items(), key=lambda x: x[1], reverse=True)[0]
    return number, times

# number, times = get_counts(array)
# print(f"Номер {number} подсчитывается {times} раз(а) в массиве.")

# cProfile.run('get_counts(array)')
#       206 function calls in 22.616 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000   22.616   22.616 <string>:1(<module>)
#      1   22.616   22.616   22.616   22.616 less4_prob1b.py:14(get_counts)
#    200    0.000    0.000    0.000    0.000 less4_prob1b.py:23(<lambda>)
#      1    0.000    0.000   22.616   22.616 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {built-in method builtins.sorted}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#      1    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}
