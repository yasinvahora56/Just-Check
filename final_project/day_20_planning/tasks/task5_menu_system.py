# Task 5: Menu System (Working Base Version)
# Run this file using the command: python task5_menu_system.py

# Instructions:
# Combine all the functions into a while loop menu system.
# This represents the completed "Day 20" base version of the project.

import json
import os

FILE_NAME = "expenses.json"

def load_data():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            pass
    return []

def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

def add_expense(expenses):
    try:
        amount = float(input("Enter expense amount: "))
        category = input("Enter category: ").strip()
        expenses.append({"amount": amount, "category": category.title()})
        save_data(expenses)
        print("Expense added successfully!")
    except ValueError:
        print("Invalid input for amount.")

def view_expenses(expenses):
    print("\n--- Expense List ---")
    if not expenses:
        print("No expenses found.")
        return
    for i, exp in enumerate(expenses, 1):
        print(f"{i}. {exp['category']} - ${exp['amount']}")

def calculate_total(expenses):
    total = sum(exp["amount"] for exp in expenses)
    print(f"\nTotal Expenses: ${total:.2f}")

def main():
    expenses = load_data()
    
    while True:
        print("\n--- Expense Tracker Menu ---")
        print("1. Add Data (Expense)")
        print("2. View Data (Expenses & Total)")
        print("3. Exit")
        
        choice = input("Enter choice (1-3): ")
        
        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            view_expenses(expenses)
            calculate_total(expenses)
        elif choice == '3':
            print("Exiting tracker. Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
