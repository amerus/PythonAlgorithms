'''
Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560, в нем 3 четные
цифры (4, 6 и 0) и 2 нечетные (3 и 5).
'''

number = input("Please, enter a number: \t")
even_counter = 0
for i in number:
    if int(i) % 2 == 0:
        even_counter += 1
print(f'There are {even_counter} even numbers and {len(number)-even_counter} odd numbers in {number}.')
