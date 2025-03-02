import random

while True:
    top_range = input("🎯 Enter a number (greater than 0): ")
    
    if top_range.isdigit():
        top_range = int(top_range)
        if top_range > 0:
            break
        else:
            print("⚠️ Please enter a number greater than 0!")
    else:
        print("❌ Invalid input! Please enter a number.")

# Generate a random number between 0 and top_range
random_number = random.randint(0, top_range)
guess_count = 0

print("\n🎲 Let's start! Try to guess the number.\n")

while True:
    guess_count += 1
    user_guess = input(f"🔢 Attempt {guess_count} - Make a guess: ")

    if not user_guess.isdigit():
        print("⚠️ Please enter a valid number!")
        continue

    user_guess = int(user_guess)

    if user_guess == random_number:
        print(f"\n🎉 Correct! You guessed the number in {guess_count} attempts. Well done! 🏆")
        break
    elif user_guess < random_number:
        print("⬆️ Too low! Try a higher number.")
    else:
        print("⬇️ Too high! Try a lower number.")
