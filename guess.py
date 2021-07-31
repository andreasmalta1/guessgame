# A high or low guessing game
# There are two versions of the game - user_guess or computer_guess.
# In user_guess the user has to to guess the random generated number which cab be between any chosen range
# With each guess, the computer responds whether the guess is too low, too high or correct
# In computer_guess the user thinks of a number and the the computer will try to guess using random numbers
# The user responds with high, low or correct

import random


# The user tries to guess
def user_guess(x):
    random_number = random.randint(1, x)  # Generating random number from 1 to x
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_number:
            print("Too low")
        if guess > random_number:
            print("Too high")

    print(f"You guessed the number {random_number} correctly")


# Computer tries to guess
def computer_guess(x):
    # Initially the low number is 1 and the high is the highest number
    # With each guess and user response, the range of options for the computer to guess will get stricter
    low = 1
    high = x
    feedback = ""
    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f"Is {guess} too high (H), too low (L) or correct (C)?: ").lower()
        if feedback == "h":
            high = guess - 1
        if feedback == "l":
            low = guess + 1
    print(f"Computer guessed {guess}")


# computer_guess(1000)
user_guess(100)

