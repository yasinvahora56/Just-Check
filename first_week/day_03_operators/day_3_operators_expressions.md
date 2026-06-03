# Day 3: Operators & Expressions

Welcome to Day 3! Today, we are learning about **Operators** and **Expressions** in Python. 

An **operator** is a special symbol (like `+`, `-`, `*`, etc.) that performs an operation on values or variables. The values the operator works on are called **operands**.

For example, in the expression `10 + 5`:
- `+` is the **operator**.
- `10` and `5` are the **operands**.

---

## 1. Arithmetic Operators
These operators are used to perform basic mathematical operations like addition, subtraction, multiplication, and division.

| Operator | Name | Description | Example | Result |
| :---: | :--- | :--- | :--- | :--- |
| `+` | Addition | Adds two numbers | `10 + 5` | `15` |
| `-` | Subtraction | Subtracts the second number from the first | `10 - 5` | `5` |
| `*` | Multiplication | Multiplies two numbers | `10 * 5` | `50` |
| `/` | Division | Divides first number by second (always returns a decimal/float) | `10 / 4` | `2.5` |
| `//` | Floor Division | Divides and rounds down to the nearest whole number | `10 // 4` | `2` |
| `%` | Modulus | Returns the remainder left after division | `10 % 3` | `1` |
| `**` | Exponentiation | Calculates the power (left raised to power of right) | `2 ** 3` | `8` |

### Detailed Examples:

*   **Division (`/`) vs. Floor Division (`//`)**:
    *   `/` always gives a float value (e.g., `5 / 2` is `2.5`).
    *   `//` chops off the decimal part and returns an integer (e.g., `5 // 2` is `2`).
    
    ```python
    x = 7
    y = 3
    
    print(x / y)   # Output: 2.3333333333333335 (Float Division)
    print(x // y)  # Output: 2 (Floor Division - rounds down)
    ```

*   **Modulus (`%`)**:
    This is very useful for checking if a number is **Even** or **Odd**. If a number `% 2` is `0`, it is even. If it is `1`, it is odd.
    
    ```python
    print(10 % 3)  # Output: 1 (because 3 * 3 = 9, remainder is 1)
    print(10 % 2)  # Output: 0 (10 is perfectly divisible by 2)
    print(11 % 2)  # Output: 1 (11 is not perfectly divisible by 2, so it's odd)
    ```

*   **Exponentiation (`**`)**:
    Used to calculate power.
    
    ```python
    print(3 ** 2)  # Output: 9 (3 raised to the power of 2, or 3 * 3)
    print(2 ** 4)  # Output: 16 (2 * 2 * 2 * 2)
    ```

---

## 2. Comparison (Relational) Operators
Comparison operators compare two values and decide the relation between them. They always return a **boolean** value: either `True` or `False`.

| Operator | Meaning | Example | Result |
| :---: | :--- | :--- | :--- |
| `==` | Equal to | `5 == 5` | `True` |
| `!=` | Not equal to | `5 != 3` | `True` |
| `>` | Greater than | `5 > 8` | `False` |
| `<` | Less than | `5 < 8` | `True` |
| `>=` | Greater than or equal to | `5 >= 5` | `True` |
| `<=` | Less than or equal to | `4 <= 3` | `False` |

### Detailed Examples:

```python
a = 15
b = 10

print(a == b)  # Output: False (15 is not equal to 10)
print(a != b)  # Output: True  (15 is indeed not equal to 10)
print(a > b)   # Output: True  (15 is greater than 10)
print(a <= b)  # Output: False (15 is not less than or equal to 10)
```

---

## 3. Logical Operators
Logical operators are used to combine multiple conditions. In Python, there are three logical operators: `and`, `or`, and `not`.

### 1. `and` Operator
Returns `True` **only if both** conditions are `True`. If even one condition is `False`, the result is `False`.

| Condition 1 | Condition 2 | Result |
| :---: | :---: | :---: |
| `True` | `True` | `True` |
| `True` | `False` | `False` |
| `False` | `True` | `False` |
| `False` | `False` | `False` |

```python
x = 5
# Both conditions must be True
print(x > 3 and x < 10)  # Output: True (because 5 > 3 is True and 5 < 10 is True)
print(x > 6 and x < 10)  # Output: False (because 5 > 6 is False)
```

### 2. `or` Operator
Returns `True` if **at least one** of the conditions is `True`. It only returns `False` if both conditions are `False`.

| Condition 1 | Condition 2 | Result |
| :---: | :---: | :---: |
| `True` | `True` | `True` |
| `True` | `False` | `True` |
| `False` | `True` | `True` |
| `False` | `False` | `False` |

```python
x = 5
# Only one condition needs to be True
print(x > 6 or x < 10)  # Output: True (x < 10 is True, even though x > 6 is False)
print(x > 10 or x < 2)  # Output: False (Both conditions are False)
```

### 3. `not` Operator
Used to reverse the logical state of a condition. It turns `True` to `False`, and `False` to `True`.

```python
is_sunny = True
print(not is_sunny)  # Output: False

x = 5
print(not(x > 10))  # Output: True (since x > 10 is False, not(False) becomes True)
```

---

## 4. Assignment Operators (Extra Concept)
Assignment operators are used to assign values to variables. You can also combine them with arithmetic operators to write shorter code.

| Operator | Example | Equivalent to | Explanation |
| :---: | :--- | :--- | :--- |
| `=` | `x = 5` | `x = 5` | Assigns value `5` to `x` |
| `+=` | `x += 3` | `x = x + 3` | Adds `3` to `x` and saves the result in `x` |
| `-=` | `x -= 2` | `x = x - 2` | Subtracts `2` from `x` and saves the result in `x` |
| `*=` | `x *= 4` | `x = x * 4` | Multiplies `x` by `4` and saves the result in `x` |
| `/=` | `x /= 2` | `x = x / 2` | Divides `x` by `2` and saves the result in `x` |

```python
num = 10
num += 5   # num = num + 5 -> 10 + 5
print(num) # Output: 15

num *= 2   # num = num * 2 -> 15 * 2
print(num) # Output: 30
```

---

## 5. Operator Precedence (Rules of Order)
When you have multiple operators in a single expression, Python evaluates them in a specific order. This is similar to the **BODMAS** / **PEMDAS** rule in mathematics.

1.  **Parentheses `()`** (Highest Priority)
2.  **Exponentiation `**`**
3.  **Multiplication `*`, Division `/`, Floor Division `//`, Modulus `%`**
4.  **Addition `+`, Subtraction `-`**
5.  **Comparison Operators (`==`, `!=`, `>`, etc.)**
6.  **Logical Operators (`not`, then `and`, then `or`)** (Lowest Priority)

```python
# Example:
result = 10 + 2 * 3
# Multiplication (*) is done first: 2 * 3 = 6
# Then addition (+): 10 + 6 = 16
print(result)  # Output: 16

# Using parentheses to change order:
result2 = (10 + 2) * 3
# Parentheses are done first: 10 + 2 = 12
# Then multiplication: 12 * 3 = 36
print(result2)  # Output: 36
```

---

## Practice Tasks
Navigate to the [tasks/](./tasks/) folder to complete today's assignments:
*   [Task 1: Basic Operations](./tasks/task1_basic_operations.py)
*   [Task 2: Even or Odd](./tasks/task2_even_odd.py)
*   [Task 3: Largest of 3 Numbers](./tasks/task3_largest_of_three.py)
*   [Task 4: Eligibility Checker](./tasks/task4_eligibility_checker.py)
*   [Task 5: Profit or Loss Calculator](./tasks/task5_profit_loss.py)
