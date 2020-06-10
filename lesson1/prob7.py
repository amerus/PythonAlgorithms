'''
Определить, является ли год, который ввел пользователь, високосным или не високосным.
'''

year = input("Введите четырехзначное значение года: \t")

if year.isdigit():
    year = int(year)

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("yes")
            exit(0)
        print("no")
        exit(0)
    print("yes")
