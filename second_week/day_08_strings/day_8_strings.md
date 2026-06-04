# Day 8: Strings

Welcome to Day 8! Strings are one of the most-used data types in Python. A **string** is simply a sequence of characters — letters, numbers, symbols — enclosed in quotes.

---

## 1. What Is a String?

```python
name = "Python"
greeting = 'Hello, World!'
empty = ""           # An empty string has 0 characters
multiline = """This
spans multiple
lines."""
```

> Strings are **immutable** — once created, you cannot change an individual character. You must create a new string instead.

---

## 2. String Indexing – Accessing Individual Characters

Every character in a string has a position called an **index**, starting at `0`.

```
String:  P  y  t  h  o  n
Index:   0  1  2  3  4  5
         -6 -5 -4 -3 -2 -1  (negative indices count from the end)
```

```python
word = "Python"

print(word[0])   # 'P'   (first character)
print(word[3])   # 'h'   (fourth character)
print(word[-1])  # 'n'   (last character — negative indexing!)
print(word[-2])  # 'o'   (second-to-last character)
```

> ⚠️ If you try `word[10]` on a 6-letter string, Python raises an **IndexError**. Always stay within bounds!

---

## 3. String Slicing – Getting a Portion

Slicing lets you extract a **substring** (a piece of the string).

### Syntax: `string[start : stop : step]`
- `start` → index to begin (inclusive, default is 0)
- `stop`  → index to end (exclusive, NOT included)
- `step`  → how many characters to jump (default is 1)

```python
word = "Python"

print(word[0:3])   # 'Pyt'   → characters at index 0, 1, 2 (stop=3 is excluded)
print(word[2:5])   # 'tho'   → characters at index 2, 3, 4
print(word[:4])    # 'Pyth'  → from start up to (not including) index 4
print(word[2:])    # 'thon'  → from index 2 to the very end
print(word[:])     # 'Python'→ full copy of the string
print(word[::-1])  # 'nohtyP'→ reversed string! (step = -1 goes backwards)
```

### Slicing Trick — Reversing a String:
```python
text = "hello"
reversed_text = text[::-1]
print(reversed_text)  # Output: olleh
```
> `[::-1]` means: start from the end, go backwards one step at a time.

---

## 4. String Methods – Built-in Tools

Python provides many built-in methods to work with strings. Methods are called using a dot (`.`) after the string.

### `upper()` and `lower()`
Convert the entire string to uppercase or lowercase.
```python
text = "Hello World"
print(text.upper())   # 'HELLO WORLD'
print(text.lower())   # 'hello world'
```

### `strip()`, `lstrip()`, `rstrip()`
Remove whitespace (spaces, tabs) from the string.
```python
text = "   hello   "
print(text.strip())    # 'hello'  (removes from both sides)
print(text.lstrip())   # 'hello   ' (removes from left only)
print(text.rstrip())   # '   hello'  (removes from right only)
```

### `replace(old, new)`
Replace every occurrence of `old` with `new`.
```python
text = "I love cats. Cats are great."
print(text.replace("cats", "dogs"))  # 'I love dogs. Cats are great.'
# Note: replace() is CASE-SENSITIVE. 'Cats' was NOT replaced.
print(text.replace("cats", "dogs").replace("Cats", "Dogs"))  # Both replaced
```

### `find(substring)`
Returns the **index** of the first occurrence of the substring. Returns `-1` if not found.
```python
text = "Hello World"
print(text.find("World"))  # 6  (W is at index 6)
print(text.find("xyz"))    # -1 (not found)
```

### `split(separator)`
Splits the string into a **list** of parts wherever the separator appears.
```python
sentence = "apple,banana,cherry"
fruits = sentence.split(",")
print(fruits)  # ['apple', 'banana', 'cherry']

words = "Hello World Python".split(" ")
print(words)   # ['Hello', 'World', 'Python']
```

### `join(list)`
Joins a list of strings into one string, inserting the separator between each item.
```python
words = ["Hello", "World", "Python"]
result = " ".join(words)
print(result)  # 'Hello World Python'
```

### `len()` – Length of a String (not a method, a built-in function)
```python
text = "Python"
print(len(text))  # 6
```

### `in` – Check if substring exists
```python
text = "I love Python"
print("Python" in text)    # True
print("Java" in text)      # False
```

### `startswith()` and `endswith()`
```python
text = "Hello World"
print(text.startswith("Hello"))  # True
print(text.endswith("World"))    # True
print(text.endswith("Python"))   # False
```

---

## 5. Counting Vowels – Practical Example

```python
text = "education"
vowels = "aeiouAEIOU"
count = 0

for char in text:      # Loop through each character
    if char in vowels: # Check if this character is a vowel
        count += 1

print(f"Vowels = {count}")  # Vowels = 5
```

---

## 6. f-Strings – Modern Way to Format Strings

f-strings (formatted string literals) let you embed Python expressions directly inside strings.

```python
name = "Alice"
age = 20
city = "Delhi"

# Old way (concatenation):
print("My name is " + name + " and I am " + str(age) + " years old.")

# New way (f-string): much cleaner!
print(f"My name is {name} and I am {age} years old.")
print(f"I live in {city.upper()}")  # You can call methods inside {}!
print(f"5 + 3 = {5 + 3}")           # You can do math inside {}!
```

---

## Practice Tasks
Navigate to the [tasks/](./tasks/) folder to complete today's assignments:
* [Task 1: Reverse a String](./tasks/task1_reverse_string.py)
* [Task 2: Palindrome Checker](./tasks/task2_palindrome.py)
* [Task 3: Count Vowels](./tasks/task3_count_vowels.py)
* [Task 4: Password Validator](./tasks/task4_password_validator.py)
* [Task 5: String Formatter](./tasks/task5_string_formatter.py)
