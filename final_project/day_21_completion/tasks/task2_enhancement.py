# Task 2: Feature Enhancement
# Run this file using the command: python task2_enhancement.py

# Instructions:
# Let's add a new feature: Deleting an expense.
# To delete an expense, we need to show the list, ask the user which number they want to delete,
# and safely remove it using `.pop()`.

# ----------------- Write Your Code Below -----------------

def delete_expense(expenses):
    print("\n--- Delete Expense ---")
    if not expenses:
        print("No expenses to delete.")
        return

    # First, display them so the user knows what numbers to choose
    for i, exp in enumerate(expenses, 1):
        print(f"{i}. {exp['category']} - ${exp['amount']:.2f}")

    try:
        choice = int(input("\nEnter the number of the expense to delete: "))
        
        # Validate the index!
        if 1 <= choice <= len(expenses):
            # .pop() removes the item at the given index. 
            # We use choice-1 because humans count from 1, but Python counts from 0.
            removed = expenses.pop(choice - 1)
            print(f"Successfully deleted {removed['category']} expense of ${removed['amount']:.2f}.")
        else:
            print("Error: Invalid number. That expense does not exist.")
            
    except ValueError:
        print("Error: Please enter a valid number.")

# Simulating the feature
if __name__ == "__main__":
    sample_data = [
        {"amount": 50, "category": "Food"},
        {"amount": 100, "category": "Travel"}
    ]
    delete_expense(sample_data)
    print("\nRemaining data:", sample_data)
