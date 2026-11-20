import random


def play_game():
    print("\n=== Welcome to Number Guessing Game ===")
    print("I'm thinking of a number between 1 and 100.")
    print("You have 7 attempts to guess it!\n")

    secret_number = random.randint(1, 100)
    max_attempts = 7
    attempts = 0

    while attempts < max_attempts:
        remaining = max_attempts - attempts
        guess_input = input(
            f"Attempt {attempts + 1}/{max_attempts} ({remaining} left) - Enter your guess: "
        ).strip()

        if not guess_input.isdigit():
            print("Please enter a valid whole number.\n")
            continue

        guess = int(guess_input)
        attempts += 1

        if guess < secret_number:
            print("Too low! Try a higher number.\n")
        elif guess > secret_number:
            print("Too high! Try a lower number.\n")
        else:
            print(
                f"🎉 Correct! You guessed {secret_number} in {attempts} {'try' if attempts == 1 else 'tries'}!\n"
            )
            break
    else:
        print(
            f"💀 Out of attempts! The secret number was {secret_number}.\n"
        )


def main():
    while True:
        play_game()
        again = input("Play again? (y/n): ").strip().lower()
        if again not in ("y", "yes"):
            print("Thanks for playing! Goodbye.")
            break


if __name__ == "__main__":
    main()