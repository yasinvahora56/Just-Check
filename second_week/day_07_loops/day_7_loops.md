# Day 7: Loops (for, while)

Welcome to Day 7! Today we enter the world of **repetition**. Loops are one of the most powerful tools in programming — they let you run the same block of code many times without writing it again and again.

---

## Why Do We Need Loops?

Imagine you want to print "Hello" 100 times. Without loops, you'd need 100 `print()` statements. With a loop, you write it once and tell Python to repeat it 100 times. That's the power of loops!

---

## 1. The `for` Loop

A `for` loop is used when you **know in advance** how many times you want to repeat something.

### Syntax:
```python
for variable in sequence:
    # code to repeat
```

### How It Works:
- Python takes each item from the sequence one by one.
- It stores the current item in the `variable`.
- It runs the indented code block with that value.
- This repeats until the sequence is exhausted.

### Example 1 – Looping through a `range()`:
```python
for i in range(5):
    print(i)
# Output: 0 1 2 3 4
```
> **Note:** `range(5)` generates numbers `0, 1, 2, 3, 4`. It starts at `0` by default and goes **up to but NOT including** 5.

### Example 2 – `range(start, stop)`:
```python
for i in range(1, 6):
    print(i)
# Output: 1 2 3 4 5
```

### Example 3 – `range(start, stop, step)`:
```python
for i in range(0, 10, 2):
    print(i)
# Output: 0 2 4 6 8
```
> The third argument `step=2` means "jump by 2 each time".

### Example 4 – Looping through a string:
```python
for letter in "Python":
    print(letter)
# Output: P y t h o n  (each letter on a new line)
```

---

## 2. The `while` Loop

A `while` loop is used when you **don't know in advance** how many times to repeat — you keep looping as long as a condition remains `True`.

### Syntax:
```python
while condition:
    # code to repeat
```

### How It Works:
1. Python checks the condition.
2. If it's `True`, the code inside runs.
3. After the code runs, Python checks the condition again.
4. This repeats until the condition becomes `False`.

### Example 1 – Simple countdown:
```python
count = 1
while count <= 5:
    print(count)
    count = count + 1  # VERY IMPORTANT: update the variable!
# Output: 1 2 3 4 5
```

> ⚠️ **Infinite Loop Warning!** If you forget to update `count`, the condition `count <= 5` will always be `True` and the program will run forever! Always make sure your `while` loop's condition eventually becomes `False`.

### Example 2 – Ask until valid input:
```python
answer = ""
while answer != "yes":
    answer = input("Do you agree? (yes/no): ")
print("Thank you!")
```

---

## 3. `break` – Exit the Loop Early

The `break` statement **immediately stops** the loop, even if the condition is still `True` or the sequence isn't finished.

### Example:
```python
for i in range(1, 11):
    if i == 5:
        break       # Stop the loop when i reaches 5
    print(i)
# Output: 1 2 3 4
```
> As soon as `i` becomes `5`, `break` is triggered and we exit the loop. `5` itself is never printed.

---

## 4. `continue` – Skip to the Next Iteration

The `continue` statement **skips the rest of the current loop iteration** and jumps back to the top to check the condition / get the next item.

### Example – Print numbers, but skip 3:
```python
for i in range(1, 6):
    if i == 3:
        continue    # Skip this iteration when i is 3
    print(i)
# Output: 1 2 4 5
```
> When `i == 3`, `continue` fires and we jump to `i = 4`. The number `3` is never printed.

---

## 5. Nested Loops (Loop inside a Loop)

You can put a loop inside another loop. The inner loop completes all its iterations for every single iteration of the outer loop.

### Example – Multiplication grid:
```python
for i in range(1, 4):       # Outer loop: runs 3 times
    for j in range(1, 4):   # Inner loop: runs 3 times for EACH outer
        print(i * j, end=" ")
    print()   # Move to next line after inner loop finishes
# Output:
# 1 2 3
# 2 4 6
# 3 6 9
```

---

## Quick Comparison: `for` vs `while`

| Feature | `for` Loop | `while` Loop |
| :--- | :--- | :--- |
| **When to use** | When you know the number of repetitions | When you don't know how many times to repeat |
| **Controlled by** | A sequence or `range()` | A condition (True/False) |
| **Risk of infinite loop** | No (sequence always ends) | Yes (if condition never becomes False) |
| **Common use case** | Iterating lists, strings, ranges | User input validation, game loops |

---

## Practice Tasks
Navigate to the [tasks/](./tasks/) folder to complete today's assignments:
* [Task 1: Print Numbers 1–100](./tasks/task1_print_numbers.py)
* [Task 2: Multiplication Table](./tasks/task2_multiplication_table.py)
* [Task 3: Sum of N Numbers](./tasks/task3_sum_of_n.py)
* [Task 4: Factorial](./tasks/task4_factorial.py)
* [Task 5: Pattern Printing](./tasks/task5_pattern.py)
* [Task 6: While Loop Challenge](./tasks/task6_while_challenge.py)
