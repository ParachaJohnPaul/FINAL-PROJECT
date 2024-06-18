import time

def typing_master():
  """Challenges the user to type a displayed text, measuring time and accuracy."""

  # Sample text (replace with your desired text)
  text = "My family is very important to me. We do lots of things together. My brothers and I like to go on long walks in the mountains."

  # Clear the screen (optional)
  print("\033c")  # Clear screen on Linux/macOS (adjust for Windows if needed)

  # Display the text
  print(text)

  # Start time measurement
  start_time = time.time()

  # Get user input
  user_input = input("Type the text above: ")

  # End time measurement
  end_time = time.time()

  # Calculate elapsed time
  elapsed_time = end_time - start_time

  # Calculate accuracy
  correct_chars = 0
  for i in range(len(text)):
    if text[i] == user_input[i] and user_input[i] != ' ':  # Ignore spaces
      correct_chars += 1

  accuracy = (correct_chars / len(text)) * 100

  # Display results
  print("\n--- Results ---")
  print(f"Time taken: {elapsed_time:.2f} seconds")
  print(f"Accuracy: {accuracy:.2f}% ({correct_chars} characters correct)")

  # Optionally, provide feedback based on accuracy
  if accuracy >= 95:
    print("Excellent typing skills!")
  elif accuracy >= 85:
    print("Very good typing!")
  elif accuracy >= 75:
    print("Keep practicing, you're doing well!")
  else:
    print("Don't give up, you can improve!")

# Run the game
typing_master()
