'''
Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. Например, если введено
число 3486, надо вывести 6843.
'''

number = input("Please, enter a number: \t")

reverse = ""
for char in number:
    reverse = char + reverse
print(reverse)
