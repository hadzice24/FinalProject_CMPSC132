import random

# Prompt user until a valid integer is entered.
def get_valid_guess():
    valid = False
    
    while not valid:
        guess = input("Enter your guess (1 - 100): ")
        try:
            guess = int(guess)
            if 1 <= guess <= 100:
                valid = True
            else:
                print("Please enter a number between 1 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    return guess

# Game Logic
def play_game():
    number = random.randint(1, 100)
    attempts = 0
    guessed_correctly = False

    print()

    while not guessed_correctly:
        guess = get_valid_guess()
        attempts += 1

        if guess > number:
            print("Too high!")
        elif guess < number:
            print("Too low!")
        else:
            print("Correct! Congratulations!")
            print("You guessed it in {attempts} attempts.")
            guessed_correctly = True
