# Task 3: Mini Challenge (Word Counter)
# Run this file using the command: python task3_word_counter.py

# Instructions:
# 1. Create a file called "story.txt" and write a short 3-sentence paragraph into it.
# 2. Read the file back.
# 3. Count how many words are in the file and print the result.
# 4. Count how many times the word "the" (case-insensitive) appears.

# Concept Explained:
# To count words, we can read the file, and then use the `.split()` string method.
# `.split()` breaks a string into a list of words, using spaces as the separator.
# Then, `len(list)` gives us the word count.

# ----------------- Write Your Code Below -----------------

# Step 1: Create the file
content = "The quick brown fox jumps over the lazy dog. The dog woke up and barked at the fox. They both ran away."
with open("story.txt", "w") as file:
    file.write(content)

# Step 2: Read and Process
with open("story.txt", "r") as file:
    text = file.read()

# Step 3: Count total words
# .split() turns the string into a list of words
words_list = text.split() 
total_words = len(words_list)

print(f"Total words in file: {total_words}")

# Step 4: Count occurrences of "the"
the_count = 0
for word in words_list:
    # We use .lower() to ensure "The" and "the" are both counted
    if word.lower() == "the":
        the_count += 1

print(f"The word 'the' appears {the_count} times.")

# ---------------------------------------------------------
# Expected Output:
# Total words in file: 21
# The word 'the' appears 4 times.
