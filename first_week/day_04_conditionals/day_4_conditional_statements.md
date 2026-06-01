# 🛠️ Day 4: Conditional Statements (`if`, `elif`, `else`)

Welcome to Day 4! Today we explore decision-making. You will learn to control the flow of your program by executing specific blocks of code only when certain conditions are true.

---

## 📖 Topics to Learn

### 1. What are Conditional Statements?
Normally, Python runs code line-by-line from top to bottom. **Conditional statements** let you bypass or run chunks of code based on logical evaluations (which evaluate to `True` or `False`).

In Python, we use **Indentation (spaces)** to define code blocks instead of curly braces `{}`. Always use **4 spaces** or a **Tab** for indentation.

#### 💡 Syntax & Block Definition Comparison
See how different languages mark where a block of code starts and ends inside an `if` condition:

##### ☕ Java / C++ / JavaScript (Uses `{}`):
```javascript
if (age >= 18) {
    System.out.println("You can vote!");
    System.out.println("Congratulations!");
}
```

##### 🐍 Python (Uses Indentation & Colon `:`):
```python
if age >= 18:
    print("You can vote!")
    print("Congratulations!")
```
> **Key Difference for Students:** In other languages, curly braces `{}` define the boundary of the block, and indentation is optional (just for readability). In Python, there are **no curly braces**! The **colon (`:`)** and the **indentation level** tell Python where the block begins and ends. If you don't indent correctly, Python will throw an `IndentationError`!

---

### 2. Syntax of Conditional Blocks

#### 🅰️ Simple `if` Statement
Runs a block of code if the condition is `True`.
```python
age = 20
if age >= 18:
    print("You can vote!") # Indented block
```

#### 🅱️ `if-else` Statement
Provides an alternative block of code if the condition is `False`.
```python
age = 15
if age >= 18:
    print("You can vote!")
else:
    print("Too young to vote!")
```

#### 🆃 `if-elif-else` Ladder
Used when we have multiple conditions to check in sequence. As soon as one condition is met, the rest are skipped.
```python
marks = 75
if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B") # This runs because 75 >= 75
else:
    print("Grade: C")
```

---

### 3. Nested Conditions
You can write an `if` statement *inside* another `if` statement. This is called nesting.

```python
has_ticket = True
has_id = False

if has_ticket:
    if has_id:
        print("Welcome to the event!")
    else:
        print("Please show your ID card to enter.")
else:
    print("No ticket, no entry.")
```

---

## 📂 Practice Tasks
Go to the [tasks/](./tasks/) folder to complete today's assignments:
* [Task 1: Grade System](./tasks/task1_grade_system.py)
* [Task 2: Login System](./tasks/task2_login_system.py)
* [Task 3: ATM Simulation](./tasks/task3_atm_simulation.py)
* [Task 4: Menu Program](./tasks/task4_menu_program.py)
* [Task 5: Ticket Pricing](./tasks/task5_ticket_pricing.py)
