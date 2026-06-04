# Task 1: Debugging
# Run this file using the command: python task1_debugging.py

# Instructions:
# Improve the `add_expense` logic from Day 20.
# We need to ensure the user cannot enter a negative number or a zero for an expense.

# ----------------- Write Your Code Below -----------------

def add_expense_robust():
    while True: # Keep asking until valid
        try:
            amount = float(input("Enter expense amount: "))
            
            # Edge case handling!
            if amount <= 0:
                print("Error: Expense amount must be greater than zero.")
                continue # Jump back to the start of the while loop
                
            category = input("Enter category: ").strip()
            if not category:
                print("Error: Category cannot be empty.")
                continue
                
            print(f"Success! Added ${amount} for {category}")
            return {"amount": amount, "category": category} # Return the valid dict
            
        except ValueError:
            print("Invalid input. Please enter numbers only (e.g., 50.50).")

if __name__ == "__main__":
    print("Testing robust input:")
    new_exp = add_expense_robust()
    print("Final saved dictionary:", new_exp)

# ---------------------------------------------------------
# Expected Output (simulated):
# Testing robust input:
# Enter expense amount: -50
# Error: Expense amount must be greater than zero.
# Enter expense amount: 50
# Enter category: Food
# Success! Added $50.0 for Food
# Final saved dictionary: {'amount': 50.0, 'category': 'Food'}
