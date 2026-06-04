# Task 2: Palindrome Checker
# Run this file using the command: python task2_palindrome.py

# Instructions:
# Check if a given word is a palindrome.
# A palindrome is a word that reads the same forwards and backwards.
# Examples: madam, racecar, level, noon, civic

# Concept Explained:
# Logic: if the original string equals its reverse, it IS a palindrome.
#   "madam" reversed = "madam" → They match → Palindrome ✓
#   "hello" reversed = "olleh" → They don't match → Not a palindrome ✗

# We also use .lower() to make the check case-insensitive:
#   "Madam" and "madam" should both be considered palindromes.

# ----------------- Write Your Code Below -----------------

word = input("Enter a word: ")

# Convert to lowercase for fair comparison (Madam == madam)
word_lower = word.lower()

# Reverse the lowercased word
reversed_word = word_lower[::-1]

# Compare original (lowercase) with reversed
if word_lower == reversed_word:
    print(f"'{word}' is a Palindrome ✓")
else:
    print(f"'{word}' is NOT a Palindrome ✗")

# ---------------------------------------------------------
# Expected Output (for input 'madam'):
# Enter a word: madam
# 'madam' is a Palindrome ✓

# Expected Output (for input 'hello'):
# Enter a word: hello
# 'hello' is NOT a Palindrome ✗
