# Day 11: Functions

Welcome to Day 11! Today we learn about **Functions**. Functions are reusable blocks of code that perform a specific task. They make our code modular, organized, and easier to maintain.

---

## 1. Defining and Calling Functions

In Python, you define a function using the `def` keyword, followed by the function name, parentheses `()`, and a colon `:`.

```python
# Defining a simple function
def say_hello():
    print("Hello, welcome to Python!")

# Calling the function
say_hello()
say_hello() # You can call it as many times as you want!
```

---

## 2. Function Parameters and Arguments

Functions can accept inputs, called **parameters** or **arguments**.

```python
# Defining a function with a parameter 'name'
def greet(name):
    print(f"Hello, {name}!")

# Calling the function with an argument
greet("Alice")
greet("Bob")
```

You can pass multiple parameters separated by commas.

```python
def add_numbers(num1, num2):
    sum_result = num1 + num2
    print(f"Sum = {sum_result}")

add_numbers(10, 20)  # Output: Sum = 30
```

---

## 3. Return Values

A function can send back a result to the caller using the `return` statement. Once a `return` statement is executed, the function immediately exits.

```python
def multiply(a, b):
    result = a * b
    return result

# The returned value can be stored in a variable
ans = multiply(5, 4)
print(f"Answer is {ans}") # Answer is 20
```

> **Why use `return` instead of `print()`?**
> If a function `print`s a value, you can only see it. If it `return`s a value, you can use that value later in your code (e.g., for further calculations).

---

## 4. Default Parameters

You can provide default values for parameters. If the caller doesn't provide an argument, the default value is used.

```python
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet("John") # Output: Hello, John!
greet()       # Output: Hello, Guest! (Uses default)
```

---

## 5. Why Use Functions? (Modularity)

Functions allow you to break down a complex problem into smaller, manageable pieces. 

Instead of writing a massive block of code:
```python
# Messy Code
print("Starting...")
# ... 50 lines of logic ...
print("Done logic 1")
# ... 50 lines of logic ...
print("Done logic 2")
```

You organize it with functions:
```python
# Clean, Modular Code
def initialize():
    print("Starting...")

def process_data():
    # ... logic ...
    pass

def save_data():
    # ... logic ...
    pass

initialize()
process_data()
save_data()
```

---

## Practice Tasks
Navigate to the [tasks/](./tasks/) folder to complete today's assignments:
* [Task 1: Simple Function](./tasks/task1_simple_function.py)
* [Task 2: Function for Even/Odd](./tasks/task2_even_odd.py)
* [Task 3: Grade Function](./tasks/task3_grade_function.py)
* [Task 4: Reusable Calculator](./tasks/task4_reusable_calculator.py)
* [Task 5: Challenge (Prime Check)](./tasks/task5_prime_check.py)
