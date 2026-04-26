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
