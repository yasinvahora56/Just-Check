# Task 4: Data Storage
# Run this file using the command: python task4_data_storage.py

# Instructions:
# Add JSON file handling to save and load data permanently.

# ----------------- Write Your Code Below -----------------

import json
import os

FILE_NAME = "expenses.json"

def load_data():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("Warning: JSON file corrupted. Starting fresh.")
    return []

def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)
    print("Data saved successfully.")

# Simulating the storage logic
if __name__ == "__main__":
    print("Loading data...")
    expenses = load_data()
    print(f"Loaded {len(expenses)} existing records.")
    
    # Simulate adding data
    expenses.append({"amount": 150, "category": "Groceries"})
    
    print("Saving data...")
    save_data(expenses)
