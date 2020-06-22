'''
Определить, какое число в массиве встречается чаще всего.
'''

import cProfile
from random import randint

# Original code unchanged: 100 loops, best of 5: 5.8 nsec per loop
# array = [randint(-100, 100) for _ in range(100000000)]

# Substituting list comprehension with tuple(): 100 loops, best of 5: 5.5 nsec per loop
array = tuple(randint(-100, 100) for _ in range(100000000))

def get_counts(arr: list):
    element_counter = {}
    for item in array:
        if item in element_counter:
            element_counter[item] += 1
        else:
            element_counter[item] = 1

    number, times = sorted(element_counter.items(), key=lambda x: x[1], reverse=True)[0]
    return number, times


#number, times = get_counts(array)
#print(f"Номер {number} подсчитывается {times} раз(а) в массиве.")

# cProfile.run('get_counts(array)')
#       207 function calls in 10.803 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000   10.803   10.803 <string>:1(<module>)
#      1   10.803   10.803   10.803   10.803 less4_prob1a.py:14(get_counts)
#    201    0.000    0.000    0.000    0.000 less4_prob1a.py:22(<lambda>)
#      1    0.000    0.000   10.803   10.803 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {built-in method builtins.sorted}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#      1    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}
