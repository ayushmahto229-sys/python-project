
import random

print("===== NUMBER GUESSING GAME =====")

while True:
    # Fixed number for testing
    secret_number = 42

    # For random game, use:
    # secret_number = random.randint(1, 100)

    attempts = 5

    while attempts > 0:
        try:
            guess = int(input("Enter your guess (1-100): "))

            if guess < 1 or guess > 100:
                print("Out of range. Enter a number between 1 and 100.")
                print("Attempts left:", attempts)
                continue

            attempts -= 1

            if guess == secret_number:
                print("Congratulations! You guessed it!")
                break

            elif guess < secret_number:
                print("Too low! Attempts left:", attempts)

            else:
                print("Too high! Attempts left:", attempts)

        except ValueError:
            print("Invalid input. Enter a whole number.")
            print("Attempts left:", attempts)

    else:
        print("Game Over! The number was", secret_number)

    play_again = input("Play again? (y/n): ").lower()

    if play_again != 'y':
        print("Thanks for playing!")
        break
