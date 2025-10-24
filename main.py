import random


def guess_number():
    print("Игра 'Угадай число'!")
    number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Угадайте число от 1 до 100: "))
            attempts += 1

            if guess < number:
                print("Загаданное число больше!")
            elif guess > number:
                print("Загаданное число меньше!")
            else:
                print(f"Поздравляю! Вы угадали число за {attempts} попыток!")
                break

        except ValueError:
            print("Пожалуйста, введите целое число!")


if __name__ == "__main__":
    guess_number()