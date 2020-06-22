"""
Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна принимать на
вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.
"""
import cProfile
import math
from random import randint

# 100 loops, best of 5: 5.42 nsec per loop
array = tuple(randint(1, 1000) for _ in range(1000000))

# Функция поиска верхней грани массива по номеру запрошенного простого числа
def upper_bound_for_p_n(n):
    if n < 6:
        return 100
    return math.ceil(n * (math.log(n) + math.log(math.log(n))))

def get_primary(arr: list):
    for item in array:

        n = upper_bound_for_p_n(item)

        sieve = [i for i in range(n)]
        sieve[1] = 0

        for i in range(2, n):

            if sieve[i] != 0:
                j = i * 2

                while j < n:
                    sieve[j] = 0
                    j += i

        result = [i for i in sieve if i != 0]
        return result

get_primary(array)

# cProfile.run('get_primary(array)')
#       11 function calls in 0.000 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#      1    0.000    0.000    0.000    0.000 less4_prob2a.py:13(upper_bound_for_p_n)
#      1    0.000    0.000    0.000    0.000 less4_prob2a.py:18(get_primary)
#      1    0.000    0.000    0.000    0.000 less4_prob2a.py:23(<listcomp>)
#      1    0.000    0.000    0.000    0.000 less4_prob2a.py:35(<listcomp>)
#      1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {built-in method math.ceil}
#      3    0.000    0.000    0.000    0.000 {built-in method math.log}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
