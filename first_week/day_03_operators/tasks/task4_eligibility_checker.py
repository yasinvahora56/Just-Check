# Task 4: Eligibility Checker
# Run this file using the command: python task4_eligibility_checker.py

# Instructions:
# Check if a user is eligible to vote based on two conditions:
# 1. Age must be greater than 18
# 2. Must possess a valid ID (input: "yes" or "no")
# Use the logical `and` operator.

# ----------------- Write Your Code Below -----------------

age = int(input("Enter your age: "))
has_id = input("Do you have a valid ID? (yes/no): ").lower()

# Condition: Age > 18 AND has ID
if age > 18 and has_id == "yes":
  print("Eligible")
else:
  print("Not Eligible")

# ---------------------------------------------------------
# Expected Output (e.g. for age 20 and yes):
# Enter your age: 20
# Do you have a valid ID? (yes/no): yes
# Eligible
