# Day 5: Practice & Debugging Techniques

Welcome to Day 5! Today is centered around developing real-world debugging capabilities, identifying logical errors, and building algorithms using your collective knowledge.

---

## Topics to Learn

### 1. How to Debug Like a Pro
Errors are a natural part of coding! As a software developer, you'll spend more time fixing code than writing it.
There are three main categories of errors:

1. **Syntax Errors**: Breaking the grammar rules of Python (e.g., missing parenthesis, missing colon, unmatched quotes). The code won't run at all.
2. **Runtime Errors (Exceptions)**: Code runs, but encounters an error that makes it crash during execution (e.g., dividing by zero `10 / 0`, converting letters to numbers `int("abc")`).
3. **Logical Errors (Bugs)**: Code runs successfully without crashing, but outputs the wrong result because your mathematical or conditional logic is incorrect.

#### Debugging Checklist
* Read the **Error Message** and the **Line Number** in the VS Code terminal.
* Use `print()` statements to print variable values and see what's happening at different steps.
* Comment out lines using `#` to isolate where the bug is.

---

### 2. Random Number Generation
In Python, we can generate a random number using the built-in `random` module.
```python
import random

# Generates a random number between 1 and 100 (inclusive)
secret_number = random.randint(1, 100)
```

---

### 3. Digit Operations
Mathematical operations like `% 10` and `// 10` are extremely useful for dissecting numbers:
* **`num % 10`** gives the **last digit** of a number.
 * *Example:* `123 % 10` `3`
* **`num // 10`** **removes the last digit** from a number.
 * *Example:* `123 // 10` `12`

---

## Practice Tasks
Go to the [tasks/](./tasks/) folder to complete today's practice challenges:
* [Task 1: Fix Errors](./tasks/task1_fix_errors.py)
* [Task 2: Number Guessing Game](./tasks/task2_number_guessing.py)
* [Task 3: Reverse a Number](./tasks/task3_reverse_number.py)
* [Task 4: Sum of Digits](./tasks/task4_sum_of_digits.py)
* [Task 5: Multiplication Table](./tasks/task5_multiplication_table.py)
