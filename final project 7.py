# Define game board
board = [' '] * 9

def display_board():
  """Prints the current state of the tic-tac-toe board"""
  for i in range(3):
    print('|', board[i*3], '|', board[i*3 + 1], '|', board[i*3 + 2], '|')

def is_valid_move(move):
  """Checks if a move is valid (within board range and empty space)"""
  return move >= 0 and move <= 8 and board[move] == ' '

def make_move(player, move):
  """Places the player's mark on the board at the specified move"""
  global board
  board[move] = player

def has_won(player):
  """Checks if a player has won by forming a row, column, or diagonal"""
  win_conditions = ((0, 1, 2), (3, 4, 5), (6, 7, 8),
                    (0, 3, 6), (1, 4, 7), (2, 5, 8),
                    (0, 4, 8), (2, 4, 6))
  for condition in win_conditions:
    if all(board[i] == player for i in condition):
      return True
  return False

def is_board_full():
  """Checks if all spaces on the board are filled"""
  return all(x != ' ' for x in board)

def main():
  # Get player names
  player1 = input("Player 1 (X): ")
  player2 = input("Player 2 (O): ")

  # Choose starting player
  current_player = player1 if input("Who wants to start? (X or O): ").upper() == 'X' else player2

  game_on = True
  while game_on:
    # Display board
    display_board()

    # Get player move
    while True:
      move = int(input(f"{current_player}'s turn (enter number 1-9): ")) - 1
      if is_valid_move(move):
        break
      else:
        print("Invalid move. Try again.")

    # Make the move
    make_move(current_player[0], move)

    # Check for win or tie
    if has_won(current_player[0]):
      display_board()
      print(f"{current_player} wins!")
      game_on = False
    elif is_board_full():
      display_board()
      print("It's a tie!")
      game_on = False

    # Switch player
    current_player = player2 if current_player == player1 else player1

  # Play again prompt
  if input("Play again? (y/n): ").lower() == 'y':
    main()

if __name__ == "__main__":
  main()
