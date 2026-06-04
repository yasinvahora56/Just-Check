# Day 14: Exception Handling

Welcome to Day 14! Today we learn about **Exception Handling**. When writing real-world programs, unexpected things happen. Users enter text instead of numbers, files are missing, or servers go down. 

Instead of letting the program crash, we use **Exceptions** to catch these errors and handle them gracefully.

---

## 1. What is an Exception?

An exception is an error that occurs *during* the execution of a program (a runtime error).
If not handled, it stops the program immediately.

Examples of common exceptions:
* `ZeroDivisionError`: Dividing by zero (e.g., `5 / 0`)
* `ValueError`: Invalid conversion (e.g., `int("hello")`)
* `FileNotFoundError`: Trying to read a file that doesn't exist
* `IndexError`: Trying to access an index out of bounds in a list
* `KeyError`: Trying to access a non-existent key in a dictionary

---

## 2. The `try` and `except` Blocks

To prevent a crash, we wrap the "risky" code inside a `try` block. If an error occurs, the code jumps straight to the `except` block.

### Syntax:
```python
try:
    # Code that might cause an error
except:
    # Code to run if an error happens
```

### Example:
```python
try:
    number = int(input("Enter a number: "))
    print(f"You entered {number}")
except:
    print("Error: You did not enter a valid number!")
```

---

## 3. Handling Specific Exceptions

It is best practice to catch *specific* errors rather than using a bare `except`. This helps you know exactly what went wrong.

```python
try:
    a = 10
    b = int(input("Enter a denominator: "))
    result = a / b
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
except ValueError:
    print("Error: Please enter a valid integer!")
```
> If the user types `0`, it triggers `ZeroDivisionError`.
> If the user types `"apple"`, it triggers `ValueError`.

---

## 4. The `finally` Block

The `finally` block lets you execute code, regardless of whether an exception was raised or not. It is typically used for "clean-up" actions (like closing a file or a database connection).

```python
try:
    file = open("data.txt", "r")
    # ... reading ...
except FileNotFoundError:
    print("File not found!")
finally:
    print("This will ALWAYS print, crash or no crash.")
```

---

## 5. The `else` Block

You can also use an `else` block. Code inside the `else` block runs **only if NO errors occurred** in the `try` block.

```python
try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Invalid input.")
else:
    # Only runs if the input was successful
    print(f"Thanks for entering a valid number: {num}")
```

---

## Practice Tasks
Navigate to the [tasks/](./tasks/) folder to complete today's assignments:
* [Task 1: Safe Division](./tasks/task1_safe_division.py)
* [Task 2: Input Validation](./tasks/task2_input_validation.py)
* [Task 3: Multiple Exceptions](./tasks/task3_multiple_exceptions.py)
* [Task 4: Retry System](./tasks/task4_retry_system.py)
* [Task 5: File Error Handling](./tasks/task5_file_error_handling.py)
