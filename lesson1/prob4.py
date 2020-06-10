'''
Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.
'''

letter1 = input("Введите первую букву: \t")
letter2 = input("Введите вторую букву: \t")

letter1 = letter1.lower()
letter2 = letter2.lower()

position_of_a = ord('a')

position_of_letter1 = ord(letter1) - position_of_a + 1
position_of_letter2 = ord(letter2) - position_of_a + 1
distance_letter1_letter = abs(position_of_letter1 - position_of_letter2)

print(f"{letter1} находится на {position_of_letter1} месте в алфавите")
print(f"{letter2} находится на {position_of_letter2} месте в алфавите")
print(f"Расстояние между буквами {distance_letter1_letter} буквы")
