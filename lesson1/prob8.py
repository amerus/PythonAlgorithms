'''
Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
'''

x = input("Введите первое число:\t")
y = input("Введите второе число:\t")
z = input("Введите третье число:\t")
x = float(x)
y = float(y)
z = float(z)

if y < x and x < z:
    print(x)
if x < y and z < x:
    print(x)
if x < y and y < z:
    print(y)
if x < y and x < z and z < y:
    print(z)

