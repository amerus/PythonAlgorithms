"""
Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна принимать на
вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.
"""
import cProfile
from random import randint

# 100 loops, best of 5: 5.71 nsec per loop
array = tuple(randint(1, 1000) for _ in range(1000000))


def get_primary(arr: list):
    count = 1
    end_of_range = 2
    primes = []
    for item in array:
        n = item
        while count <= n:
            is_prime = True
            for next_number in range(2, end_of_range):
                if end_of_range % next_number == 0:
                    is_prime = False
            if is_prime:
                primes.append(end_of_range)
                count += 1
            end_of_range += 1
    return primes

get_primary(array)

# cProfile.run('get_primary(array)')
#       1004 function calls in 1.570 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    1.570    1.570 <string>:1(<module>)
#      1    1.569    1.569    1.570    1.570 less4_prob2b.py:12(get_primary)
#      1    0.000    0.000    1.570    1.570 {built-in method builtins.exec}
#   1000    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
