import random

# Prompt user until a valid integer is entered.
def get_valid_guess(min_val, max_val):
    valid = False
    
    while not valid:
        guess = input(f"Enter your guess ({min_val} - {max_val}): ")
        try:
            guess = int(guess)
            if min_val <= guess <= max_val:
                valid = True
            else:
                print(f"Please enter a number between {min_val} and {max_val}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    return guess

# Game Logic
def play_game():
    print("Welcome to the Number Guessing Game!")
    min_val, max_val = choose_difficulty()
    number = random.randint(min_val, max_val)
    attempts = 0
    guessed_correctly = False


    while not guessed_correctly:
        guess = get_valid_guess(min_val, max_val)
        attempts += 1

        if guess > number:
            print("Too high!")
        elif guess < number:
            print("Too low!")
        else:
            print("Correct! Congratulations!")
            print("You guessed it in {attempts} attempts.")
            guessed_correctly = True


# Difficulty Levels
def choose_difficulty():
    print("Choose difficulty:")
    print("1. Easy (1-50)")
    print("2. Medium (1-100)")
    print("3. Hard (1-200)")

    choice = input("Enter Choice: ")

    if choice == 1 or choice == "Easy" or choice == "easy":
        return 1, 50
    elif choice == 2 or choice == "Medium" or choice == "medium":
        return 1, 100
    elif choice == 3 or choice == "Hard" or choice == "hard":
        return 1, 200
    else:
        print("Invalid Choice. Medium difficulty defaulted")
        return 1, 100
    

# Control Replay
def main():
    play_again = True

    while play_again:
        play_game()

        response = input("Do you want to play again? (Yes/No): ")
        if response == "Yes":
            play_again = True
        else:
            play_again = False
            print("Thanks for playing!")


if __name__ == "__main__":
    main()