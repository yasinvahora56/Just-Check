# Task 1: Project Planning (1 hour)
# This is a planning document, not code!

# Instructions:
# Before writing a single line of code, define your project architecture.
# Fill out the details below for your chosen project.

# ----------------- Write Your Plan Below -----------------

## Project Name
Expense Tracker CLI

## Features List
1. Add a new expense (amount and category)
2. View all expenses
3. Calculate total expenses
4. Save data to a JSON file (Persistent Storage)
5. Interactive Menu System

## Inputs and Outputs
* **Inputs**: User choices (1-4), Expense amount (float), Expense category (string).
* **Outputs**: Formatted lists of expenses, Total sum, Success/Error messages.

## Flow of Program
1. Program starts and attempts to load existing data from `expenses.json`.
2. Display the Main Menu.
3. If user selects '1', prompt for amount and category -> Save to file.
4. If user selects '2', loop through data and print formatted expenses.
5. If user selects '3', loop through data, sum the amounts, and print total.
6. If user selects '4', exit the program gracefully.
