'''
Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
'''

x = input("Введите первое число:\t")
y = input("Введите второе число:\t")
z = input("Введите третье число:\t")

x = float(x)
y = float(y)
z = float(z)

summa = x + y + z

middle_number = summa - min(x, y, z) - max(x, y, z)

print("Среднее число {:.2f}".format(middle_number))
