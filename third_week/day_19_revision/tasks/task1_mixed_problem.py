# Task 1: Mixed Problem (File + Loops)
# Run this file using the command: python task1_mixed_problem.py

# Instructions:
# Write a program that writes the numbers 1 to 10 into a file called "numbers.txt", 
# with each number on a new line.
# Then, open the file, read the numbers, and print ONLY the even numbers.

# Concept Explained:
# Combine a `for` loop to write. 
# Combine a `for` loop to read, convert the string back to an integer, and check if it is even.

# ----------------- Write Your Code Below -----------------

# Step 1: Write numbers to file
with open("numbers.txt", "w") as file:
    for i in range(1, 11):
        file.write(f"{i}\n")

# Step 2: Read from file and print evens
print("Even numbers found in the file:")
with open("numbers.txt", "r") as file:
    for line in file:
        num = int(line.strip()) # Convert the text line into an integer
        if num % 2 == 0:
            print(num)

# ---------------------------------------------------------
# Expected Output:
# Even numbers found in the file:
# 2
# 4
# 6
# 8
# 10
