import random

def is_valid_choice(choice):
  """Checks if the user's choice is valid (rock, paper, or scissors)."""
  return choice.lower() in ["rock", "paper", "scissors"]

def determine_winner(player_choice, computer_choice):
  """Determines the winner of a single round."""
  if player_choice == computer_choice:
    return "Tie"
  elif player_choice == "rock":
    if computer_choice == "scissors":
      return "Player"
    else:
      return "Computer"
  elif player_choice == "paper":
    if computer_choice == "rock":
      return "Player"
    else:
      return "Computer"
  else:  # player_choice == "scissors"
    if computer_choice == "paper":
      return "Player"
    else:
      return "Computer"

def play_best_of_three():
  """Plays a best-of-three rock-paper-scissors game."""
  player_wins = 0
  computer_wins = 0

  while player_wins < 2 and computer_wins < 2:
    print(f"\nPlayer wins: {player_wins}, Computer wins: {computer_wins}")

    player_choice = input("Choose rock, paper, or scissors (r/p/s): ")
    while not is_valid_choice(player_choice):
      player_choice = input("Invalid choice. Choose rock, paper, or scissors (r/p/s): ")

    computer_choice = random.choice(["rock", "paper", "scissors"])

    round_winner = determine_winner(player_choice.lower(), computer_choice)

    if round_winner == "Player":
      player_wins += 1
      print("You win!")
    elif round_winner == "Computer":
      computer_wins += 1
      print("Computer wins!")
    else:
      print("It's a tie!")

  if player_wins == 2:
    print("\nYou win the best-of-three game!")
  else:
    print("\nComputer wins the best-of-three game!")

# Start the game
play_best_of_three()
