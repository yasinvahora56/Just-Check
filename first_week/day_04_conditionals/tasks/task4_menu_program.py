# Task 4: Menu Program
# Run this file using the command: python task4_menu_program.py

# 📝 Instructions:
# Present a simple mathematical menu to the user:
# 1. Add
# 2. Subtract
# Take two numbers from the user and perform the chosen operation.

# ----------------- Write Your Code Below -----------------

print("Simple Calculator Menu")
print("1. Add")
print("2. Subtract")

choice = int(input("Enter choice (1 or 2): "))

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == 1:
    result = num1 + num2
    print(f"Result: {int(result)}")
elif choice == 2:
    result = num1 - num2
    print(f"Result: {int(result)}")
else:
    print("Invalid Choice")
