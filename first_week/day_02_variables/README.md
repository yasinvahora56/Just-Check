# 📦 Day 2: Variables, Data Types & Interactive Input

Welcome to Day 2! Today we learn how a program remembers data, handles different types of information, and interacts dynamically with users.

---

## 📖 Topics to Learn

### 1. What are Variables?
Think of a **variable** as a named storage box (container) inside your computer's memory. You can store data inside it, change its value later, and reference it by its name.
* **Naming Rules in Python**:
  * Must start with a letter or an underscore (`_`).
  * Cannot start with a number.
  * Can only contain alphanumeric characters and underscores (`a-z`, `A-Z`, `0-9`, and `_`).
  * Variable names are case-sensitive (`age`, `Age`, and `AGE` are three different variables).

```python
x = 10      # 'x' is a variable storing the value 10
name = "John" # 'name' is a variable storing the text "John"
```

#### 💡 Dynamic Typing Comparison
In many programming languages (like **C++, Java**), you must declare the **type** of a variable before using it. In **Python**, you don't need to specify types.

##### ☕ Java / C++ (Statically Typed):
```java
int age = 20;
String name = "Rahul";
double salary = 45000.50;
```

##### 🐍 Python (Dynamically Typed):
```python
age = 20
name = "Rahul"
salary = 45000.50
```
> **How to explain this to students:** In Python, the interpreter looks at the value (e.g. `20` or `"Rahul"`) and automatically creates a box of the correct type. You don't have to define it!

---

### 2. Basic Data Types in Python
Python automatically detects the type of data stored. The main data types are:

| Data Type | Keyword | Description | Example |
| :--- | :--- | :--- | :--- |
| **Integer** | `int` | Whole numbers (positive, negative, or zero) without decimals. | `age = 21`, `temp = -5` |
| **Floating Point** | `float` | Numbers with decimal points. | `pi = 3.14`, `price = 99.99` |
| **String** | `str` | Textual data wrapped in quotes. | `name = "Rahul"`, `letter = 'A'` |
| **Boolean** | `bool` | Represents logical states. Can only be `True` or `False`. | `is_logged_in = True` |

To check the data type of a variable, use the `type()` function:
```python
print(type(45))  # Output: <class 'int'>
```

---

### 3. Dynamic Inputs: `input()`
The `input()` function allows the user to type something into the terminal.
* **CRITICAL RULE**: The `input()` function always takes input as a **String (`str`)**, even if the user types a number!

```python
name = input("Enter your name: ")
print("Hello", name)
```

---

### 4. Type Casting (Conversion)
Since `input()` always returns a string, we must explicitly convert the type if we want to do mathematical operations. This process is called **Type Casting**.

* **Convert to Integer**: `int("30")` -> `30`
* **Convert to Float**: `float("3.14")` -> `3.14`
* **Convert to String**: `str(100)` -> `"100"`

```python
# Converting input string to int for calculation
age = int(input("Enter your age: "))
print("Next year you will be:", age + 1)
```

---

## 📂 Practice Tasks
Go to the [tasks/](./tasks/) folder to complete today's assignments:
* [Task 1: Input and Output](./tasks/task1_input_output.py)
* [Task 2: Calculator (Input Based)](./tasks/task2_calculator.py)
* [Task 3: Type Conversion](./tasks/task3_type_conversion.py)
* [Task 4: Simple Interest Calculator](./tasks/task4_simple_interest.py)
* [Task 5: Swap Two Numbers](./tasks/task5_swap_numbers.py)
