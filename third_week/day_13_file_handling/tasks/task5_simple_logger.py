# Task 5: Simple Logger
# Run this file using the command: python task5_simple_logger.py

# Instructions:
# Create a program that simulates a simple activity logger.
# Write "User logged in" to a file named "log.txt".
# Then append "User performed action" to the same file.
# Print the final log to the screen.

# Concept Explained:
# In real applications, logs are written constantly. 
# We use append ("a") mode so we don't erase previous logs.

# ----------------- Write Your Code Below -----------------

import datetime

# Bonus: Add timestamp to make it realistic
time_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# First action
with open("log.txt", "a") as file:
    file.write(f"[{time_now}] User logged in\n")

# Second action (simulating another event)
with open("log.txt", "a") as file:
    file.write(f"[{time_now}] User performed action\n")

print("Logs written. Current logs:\n")

# Read logs
try:
    with open("log.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    pass

# ---------------------------------------------------------
# Expected Output (in console):
# Logs written. Current logs:
# 
# [2026-06-04 14:00:00] User logged in
# [2026-06-04 14:00:00] User performed action
