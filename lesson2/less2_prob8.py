'''
Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел. Количество вводимых чисел
и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.
'''
number = input("Enter a number: \t")
search_pattern = input("What number should be searched and counted? \t")
counter = 0
search_pattern = int(search_pattern)
for i in number:
    if int(i) == search_pattern:
        counter += 1
print(f"That search number occurs {counter} times in {number}.")
