# Task 5: Bank Account Challenge
# Run this file using the command: python task5_bank_account.py

# Instructions:
# Create a `BankAccount` class.
# The __init__ method should accept an initial balance (defaulting to 0).
# Create a `deposit(amount)` method that adds to the balance.
# Create a `withdraw(amount)` method that subtracts from the balance.
# Create a `display_balance()` method that prints the current balance.

# Concept Explained:
# Methods can modify the internal state (attributes) of an object.
# `self.balance += amount` changes the balance for that specific account.

# ----------------- Write Your Code Below -----------------

class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance
        
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}.")
        else:
            print("Deposit amount must be positive.")
            
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        elif amount > 0:
            self.balance -= amount
            print(f"Withdrew {amount}.")
        else:
            print("Withdraw amount must be positive.")
            
    def display_balance(self):
        print(f"Balance: {self.balance}")

# Test the class
print("--- Creating Account ---")
account = BankAccount(1000)
account.display_balance()

print("\n--- Transactions ---")
account.deposit(4500)
account.withdraw(500)
account.withdraw(10000) # Should fail

print("\n--- Final Status ---")
account.display_balance()

# ---------------------------------------------------------
# Expected Output:
# --- Creating Account ---
# Balance: 1000
# 
# --- Transactions ---
# Deposited 4500.
# Withdrew 500.
# Insufficient funds!
# 
# --- Final Status ---
# Balance: 5000
