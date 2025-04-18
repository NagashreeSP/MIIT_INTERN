import random

def number_guessing_game():
    print("\n🎯 Welcome to the Number Guessing Game! 🎯")
    lower_bound = 1
    upper_bound = 100
    secret_number = random.randint(lower_bound, upper_bound)
    attempts = 10  # Max attempts

    print(f"\nI've chosen a number between {lower_bound} and {upper_bound}. Try to guess it!")
    
    for attempt in range(1, attempts + 1):
        while True:
            try:
                guess = int(input(f"\nAttempt {attempt}/{attempts} - Enter your guess: "))
                if lower_bound <= guess <= upper_bound:
                    break
                else:
                    print(f"⚠️ Please enter a number between {lower_bound} and {upper_bound}.")
            except ValueError:
                print("❌ Invalid input! Please enter a valid number.")

        if guess < secret_number:
            print("📉 Too low! Try again.")
        elif guess > secret_number:
            print("📈 Too high! Try again.")
        else:
            print(f"\n🎉 Congratulations! You guessed the number {secret_number} in {attempt} attempts. 🏆")
            break
    else:
        print(f"\n😢 Game Over! You've used all {attempts} attempts. The correct number was {secret_number}.")

if __name__ == "__main__":
    number_guessing_game()
