# This is one of the simple python projects yet an exciting one. You can even call it a mini-game. Make a program in
# which the computer randomly chooses a number between 1 to 10, 1 to 100, or any range. Then give users a hint to guess
# the number. Every time the user guesses wrong, he gets another clue, and his score gets reduced. The clue can be
# multiples, divisible, greater or smaller, or a combination of all.

import random


def user_guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_number:
            print("Too low")
        if guess > random_number:
            print("Too high")

    print(f"You guessed the number {random_number} correctly")


def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f" Is {guess} too high (H), too low (L) or correct (C)?: ").lower()
        if feedback == "h":
            high = guess - 1
        if feedback == "l":
            low = guess + 1
    print(f"Computer guessed {guess}")


computer_guess(1000)
# user_guess(10)
