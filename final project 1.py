import random

# Set the secret number range
min_number = 1
max_number = 100

# Welcome message
print("Welcome to the Number Guessing Game!")

# Generate a random number
secret_number = random.randint(min_number, max_number)
guesses = 0  # Initialize guess counter outside the loop

# Guessing loop
while True:
  # Get user guess (with error handling)
  while True:
    try:
      guess = int(input(f"Guess a number between {min_number} and {max_number}: "))
      guesses += 1  # Increment guess count here
      break  # Exit inner loop on successful input
    except ValueError:
      print("Invalid input. Please enter a number.")

  # Check guess
  if guess == secret_number:
    print(f"Congratulations! You guessed it in {guesses} tries.")
    break
  print("Too high" if guess > secret_number else "Too low")

# Play again prompt (optional)
play_again = input("Do you want to play again? (y/n): ").lower()
if play_again != 'y':
  print("Thanks for playing!")
else:
  # Reset for new game (implicit in loop)
  print("\nStarting a new game...")
  secret_number = random.randint(min_number, max_number)
  guesses = 0  # Reset guess counter for new game