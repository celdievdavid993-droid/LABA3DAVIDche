import random


def guess_number():
    print("Здравсвтуйте! Попробуйте угадать число!")
    number = random.randint(1, 250)
    attempts = 0

    while True:
        try:
            guess = int(input("Угадайте число от 1 до 250: "))
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