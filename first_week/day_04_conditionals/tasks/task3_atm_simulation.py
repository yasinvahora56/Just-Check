# Task 3: ATM Simulation
# Run this file using the command: python task3_atm_simulation.py

# 📝 Instructions:
# Predefine a balance variable (e.g., 5000).
# Show two options: 
# 1. Check Balance
# 2. Withdraw Amount
# Based on choice:
# - If 1: display balance
# - If 2: prompt for withdraw amount. Check if balance has enough cash. If yes, perform transaction and display remaining balance. Else, display "Insufficient Balance".

# ----------------- Write Your Code Below -----------------

balance = 5000

print("Welcome to Python Bank ATM")
print("1. Check Balance")
print("2. Withdraw Amount")

choice = int(input("Enter choice (1-2): "))

if choice == 1:
    print(f"Your Balance: {balance}")
elif choice == 2:
    withdraw_amount = float(input("Enter amount to withdraw: "))
    
    if withdraw_amount <= balance:
        balance = balance - withdraw_amount
        print("Transaction Successful")
        print(f"Remaining Balance: {int(balance)}")
    else:
        print("Insufficient Balance")
else:
    print("Invalid Choice")

# ---------------------------------------------------------
# Expected Output (for withdraw 1000):
# Welcome to Python Bank ATM
# 1. Check Balance
# 2. Withdraw Amount
# Enter choice (1-2): 2
# Enter amount to withdraw: 1000
# Transaction Successful
# Remaining Balance: 4000
