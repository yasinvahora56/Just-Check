# Task 2: Login System
# Run this file using the command: python task2_login_system.py

# 📝 Instructions:
# Create predefined variables for correct username and password.
# Prompt the user for input and verify both. 
# Print "Login Successful" or "Login Failed".

# ----------------- Write Your Code Below -----------------

CORRECT_USERNAME = "admin"
CORRECT_PASSWORD = "password123"

username = input("Enter username: ")
password = input("Enter password: ")

if username == CORRECT_USERNAME and password == CORRECT_PASSWORD:
    print("Login Successful")
else:
    print("Login Failed")

# ---------------------------------------------------------
# Expected Output (Successful):
# Enter username: admin
# Enter password: password123
# Login Successful
