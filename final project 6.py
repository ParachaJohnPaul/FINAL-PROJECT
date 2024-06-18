import random

def roll_dice():
  """Simulates a dice roll and returns a random number between 1 and 6."""
  return random.randint(1, 6)

def play_round():
  """Simulates a single round of the game and returns the winner (1 or 2) or 0 for tie."""
  player1_roll = roll_dice()
  player2_roll = roll_dice()
  print(f"Player 1 rolls: {player1_roll}")
  print(f"Player 2 rolls: {player2_roll}")
  if player1_roll > player2_roll:
    return 1
  elif player1_roll < player2_roll:
    return 2
  else:
    return 0

def main():
  """Runs the best of three dice rolling game."""
  player1_wins = 0
  player2_wins = 0
  for _ in range(3):
    winner = play_round()
    if winner == 1:
      player1_wins += 1
    elif winner == 2:
      player2_wins += 1
  
  if player1_wins > player2_wins:
    print("Player 1 wins the game!")
  elif player2_wins > player1_wins:
    print("Player 2 wins the game!")
  else:
    print("It's a tie!")

if __name__ == "__main__":
  main()
