# Task 3: Core Logic Implementation
# Run this file using the command: python task3_core_logic.py

# Instructions:
# Replace the `pass` statements with actual logic for input handling.
# Build the `add_expense`, `view_expenses`, and `calculate_total` features.
# (We will add the file storage part in Task 4).

# ----------------- Write Your Code Below -----------------

expenses = []

def add_expense():
    print("\n--- Add Expense ---")
    try:
        amount = float(input("Enter amount: "))
        category = input("Enter category (e.g., Food, Travel): ").strip()
        
        # Store as a dictionary
        expense_item = {"amount": amount, "category": category.title()}
        expenses.append(expense_item)
        print("Expense added successfully!")
    except ValueError:
        print("Error: Please enter a valid number for the amount.")

def view_expenses():
    print("\n--- All Expenses ---")
    if not expenses:
        print("No expenses recorded yet.")
        return
        
    for index, exp in enumerate(expenses, start=1):
        print(f"{index}. {exp['category']}: ${exp['amount']}")

def calculate_total():
    print("\n--- Total Expenses ---")
    total = sum(exp["amount"] for exp in expenses)
    print(f"Total spent: ${total:.2f}")

# Simulating a user session for testing:
if __name__ == "__main__":
    add_expense()
    add_expense()
    view_expenses()
    calculate_total()
