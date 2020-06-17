'''
Определить, какое число в массиве встречается чаще всего.
'''

from random import randint

array = [randint(0, 10) for _ in range(10)]

element_counter = {}

for item in array:
    if item in element_counter:
        element_counter[item] += 1
    else:
        element_counter[item] = 1


number, times = sorted(element_counter.items(), key=lambda x: x[1], reverse=True)[0]

print(f"Номер {number} подсчитывается {times} раз(а) в массиве {array}")

