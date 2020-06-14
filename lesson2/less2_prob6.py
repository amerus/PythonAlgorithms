'''
В программе генерируется случайное целое число от 0 до 100. Пользователь должен его отгадать не более чем за 10
попыток. После каждой неудачной попытки должно сообщаться, больше или меньше введенное пользователем число, чем то,
что загадано. Если за 10 попыток число не отгадано, вывести ответ.
'''
import random
secret_number = random.randint(0, 100)

for i in range(0,10):
    guess_number = input("What's the secret number in the zero to 100 range? \t")
    guess_number = int(guess_number)
    if guess_number == secret_number:
        print("You have guessed right!")
        break
    elif guess_number > secret_number:
        print("Try a smaller number.")
    else:
        print("Try a larger number.")
    if i == 9:
        print(f'Sorry, you have run out of attempts this time! The number was {secret_number}.')
