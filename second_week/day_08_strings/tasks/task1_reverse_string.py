# Task 1: Reverse a String
# Run this file using the command: python task1_reverse_string.py

# Instructions:
# Take a string input from the user and print it in reverse order.

# Concept Explained:
# We use Python's slicing trick: string[::-1]
#   - The first colon (:) means "from start to end" (no specific start or stop).
#   - The -1 after the second colon means "step backwards by 1".
# So [::-1] reads the string from the last character to the first — reversing it!

# Step-by-step trace for "hello":
# Original string: h e l l o
# Indices:         0 1 2 3 4
# Reversed:        o l l e h  (reading from index 4, 3, 2, 1, 0)

# ----------------- Write Your Code Below -----------------

text = input("Enter a string: ")
reversed_text = text[::-1]   # The slicing magic!

print(f"Original : {text}")
print(f"Reversed : {reversed_text}")

# ---------------------------------------------------------
# Expected Output (for input 'hello'):
# Enter a string: hello
# Original : hello
# Reversed : olleh
