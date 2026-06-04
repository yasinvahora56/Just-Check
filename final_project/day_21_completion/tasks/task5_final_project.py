# Task 5: Final Finished Project (Expense Tracker)
# Run this file using the command: python task5_final_project.py

# This is the fully polished, final version of the Expense Tracker.
# It includes JSON storage, edge-case handling, professional formatting, and the delete feature.

import json
import os

FILE_NAME = "expenses_final.json"

def load_data():
    """Loads expenses from JSON file. Returns empty list if not found."""
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("Warning: Data file corrupted. Starting fresh.")
    return []

def save_data(data):
    """Saves the expenses list to the JSON file."""
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

def add_expense(expenses):
    print("\n" + "-"*30)
    print("       ADD NEW EXPENSE       ")
    print("-"*30)
    
    while True:
        try:
            amount = float(input("Enter amount: $"))
            if amount <= 0:
                print("Amount must be greater than 0.")
                continue
                
            category = input("Enter category (e.g. Food, Rent): ").strip().title()
            if not category:
                print("Category cannot be empty.")
                continue
                
            expenses.append({"amount": amount, "category": category})
            save_data(expenses)
            print(f"Success! Added ${amount:.2f} for {category}.")
            break # Exit the loop after successful entry
            
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def view_expenses(expenses):
    print("\n" + "="*40)
    print("EXPENSE REPORT".center(40))
    print("="*40)
    
    if not expenses:
        print("No expenses recorded yet.".center(40))
        print("="*40)
        return False # Return False to indicate it's empty
        
    print(f"ID | {'Category':<20} | {'Amount':>10}")
    print("-" * 40)
    
    for i, exp in enumerate(expenses, 1):
        print(f"{i:2} | {exp['category']:<20} | ${exp['amount']:>9.2f}")
        
    print("-" * 40)
    total = sum(exp["amount"] for exp in expenses)
    print(f"{'TOTAL':<25} | ${total:>9.2f}")
    print("="*40)
    
    return True # Return True to indicate it has items

def delete_expense(expenses):
    # If view_expenses returns False (empty list), stop the deletion process early
    if not view_expenses(expenses):
        return
        
    print("\n--- Delete Expense ---")
    try:
        choice = int(input("Enter the ID of the expense to delete (or 0 to cancel): "))
        
        if choice == 0:
            print("Deletion cancelled.")
            return
            
        if 1 <= choice <= len(expenses):
            removed = expenses.pop(choice - 1)
            save_data(expenses)
            print(f"Successfully deleted {removed['category']} expense of ${removed['amount']:.2f}.")
        else:
            print("Error: Invalid ID.")
            
    except ValueError:
        print("Error: Please enter a valid number.")

def main():
    expenses = load_data()
    
    while True:
        print("\n" + "*"*30)
        print("    PERSONAL EXPENSE TRACKER   ")
        print("*"*30)
        print("1. Add Expense")
        print("2. View Expenses & Total")
        print("3. Delete Expense")
        print("4. Exit")
        print("*"*30)
        
        choice = input("Select an option (1-4): ").strip()
        
        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            view_expenses(expenses)
        elif choice == '3':
            delete_expense(expenses)
        elif choice == '4':
            print("\nSaving data... Goodbye!")
            break
        else:
            print("Invalid option. Please choose between 1 and 4.")

if __name__ == "__main__":
    main()
