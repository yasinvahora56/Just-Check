# Task 4: Simple Interest Calculator
# Run this file using the command: python task4_simple_interest.py

# 📝 Instructions:
# Prompt the user for:
# - Principal amount (P)
# - Rate of interest (R)
# - Time period in years (T)
# Calculate Simple Interest using the formula: SI = (P * R * T) / 100

# ----------------- Write Your Code Below -----------------

P = float(input("Enter Principal amount (P): "))
R = float(input("Enter Rate of Interest (R): "))
T = float(input("Enter Time in years (T): "))

# Simple Interest Formula
SI = (P * R * T) / 100

# Display simple interest
print("Simple Interest =", int(SI)) # Print as integer to match expected output or float

# ---------------------------------------------------------
# Expected Output (e.g. for P=1000, R=10, T=5):
# Enter Principal amount (P): 1000
# Enter Rate of Interest (R): 10
# Enter Time in years (T): 5
# Simple Interest = 500
