# Task 2: Number Guessing Game
# Run this file using the command: python task2_number_guessing.py

import random

# Instructions:
# Generate a random secret number between 1 and 20.
# Ask the user to guess it. Provide hints: "Too High" or "Too Low".
# Continue asking until the user guesses correctly!

# ----------------- Write Your Code Below -----------------

secret_number = random.randint(1, 20)
print("Welcome to the Number Guessing Game! I have picked a number between 1 and 20.")

while True:
  guess = int(input("Enter your guess: "))
  
  if guess > secret_number:
    print("Too High")
  elif guess < secret_number:
    print("Too Low")
  else:
    print("Correct!")
    break
