'''
Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна принимать на
вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.
'''

import cProfile
from random import randint

# 100 loops, best of 5: 5.47 nsec per loop

def is_prime(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return False
        else:
            return True
    else:
        return False


array = tuple(randint(1, 1000) for _ in range(1000000))

def get_primary(arr: list):
    primes = []
    for item in array:
        if is_prime(item):
            primes.append(item)
    return primes

get_primary(array)

# cProfile.run('get_primary(array)')
#       1168254 function calls in 3.313 seconds
#
#  Ordered by: standard name
#
#  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#       1    0.001    0.001    3.313    3.313 <string>:1(<module>)
# 1000000    3.190    0.000    3.190    0.000 less4_prob2c.py:11(is_prime)
#       1    0.113    0.113    3.312    3.312 less4_prob2c.py:24(get_primary)
#       1    0.000    0.000    3.313    3.313 {built-in method builtins.exec}
#  168250    0.008    0.000    0.008    0.000 {method 'append' of 'list' objects}
#       1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
