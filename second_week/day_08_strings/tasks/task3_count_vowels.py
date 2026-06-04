# Task 3: Count Vowels
# Run this file using the command: python task3_count_vowels.py

# Instructions:
# Take a word from the user and count how many vowels (a, e, i, o, u) it contains.

# Concept Explained:
# Vowels are: a, e, i, o, u (and their uppercase versions A, E, I, O, U)
# Strategy:
#   1. Loop through each character in the word.
#   2. Check if that character is inside the string "aeiouAEIOU".
#   3. If yes, increment the vowel counter.

# The trick: `if char in "aeiouAEIOU"` checks membership in a string!
# Python checks: is 'e' anywhere inside "aeiouAEIOU"? Yes → count it.

# Trace for "education":
# e → vowel (count=1)
# d → not a vowel
# u → vowel (count=2)
# c → not a vowel
# a → vowel (count=3)
# t → not a vowel
# i → vowel (count=4)
# o → vowel (count=5)
# n → not a vowel
# Final count = 5 ✓

# ----------------- Write Your Code Below -----------------

word = input("Enter a word: ")
vowel_count = 0
vowels = "aeiouAEIOU"

for char in word:
    if char in vowels:
        vowel_count += 1

print(f"Vowels = {vowel_count}")

# ---------------------------------------------------------
# Expected Output (for input 'education'):
# Enter a word: education
# Vowels = 5
