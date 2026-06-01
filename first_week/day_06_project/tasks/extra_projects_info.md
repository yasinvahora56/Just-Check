# Graduation Mini-Projects Guide

If you've finished the Smart Calculator, it is time to build one of these 10 mini-projects to reinforce what you've learned. You can choose any of these or work in a team!

---

### 1. Temperature Converter
* **Description**: A tool to convert temperature values back and forth.
* **Flow**:
 1. Prompt user: "Convert from (1) Celsius to Fahrenheit or (2) Fahrenheit to Celsius".
 2. Input temperature.
 3. Formula: $F = (C \times 9/5) + 32$ or $C = (F - 32) \times 5/9$.
 4. Display converted value.

---

### 2. Simple & Compound Interest Calculator
* **Description**: Compute both simple and compound interests side-by-side.
* **Formula**:
 * $SI = (P \times R \times T) / 100$
 * $CI = P \times (1 + R/100)^T - P$
* **Flow**: Take inputs $P$, $R$, and $T$ from the user and print both outcomes.

---

### 3. Student Grade Manager
* **Description**: Evaluate a student's grades over multiple subjects.
* **Flow**: Prompt for scores in Physics, Chemistry, and Mathematics. Print average, highest mark, lowest mark, and whether they passed (if all grades are above 40).

---

### 4. Basic Quiz Game
* **Description**: Create a terminal quiz of 3-5 multiple choice questions.
* **Flow**: Keep a `score` tracker starting at 0. Present each question with options A, B, C, D. If the user picks correct option, print "Correct!" and add points, else show correct answer. Print final score at the end.

---

### 5. Decimal to Binary Converter
* **Description**: Translate integer base 10 values into raw binary representation.
* **Hint**: You can use Python's built-in `bin(number)` function (which returns something like `0b1010` - slice off the `0b` prefix to show the beautiful output!). Or build a loop dividing the number by 2 repeatedly.

---

### 6. Password Strength Checker
* **Description**: Analyze password security.
* **Criteria**: Check if user password:
 1. Length is >= 8 characters.
 2. Contains at least 1 digit (hint: search password string for numbers).
 3. Contains special characters.
* **Flow**: Print strength status: "Weak", "Medium", or "Strong".

---

### 7. Bill Split Calculator
* **Description**: Split dinner bills dynamically.
* **Flow**: Ask user for total bill amount, tip percentage (e.g. 5%, 10%, 15%), and number of friends. Calculate share per person and print it beautifully.

---

### 8. Unit Converter
* **Description**: Convert units.
* **Options**:
 * Kilometers to Miles ($1\text{ km} = 0.621371\text{ miles}$)
 * Celsius to Fahrenheit
 * Kilograms to Pounds ($1\text{ kg} = 2.20462\text{ lbs}$)

---

### 9. Login System with Retry Limits
* **Description**: Secure credential form.
* **Flow**: Allow the user only **3 login attempts**. If they guess wrong 3 times, print "Locked out! Too many attempts." and exit. If they guess correctly within 3 attempts, print "Access Granted!".

---

### 10. Random Password Generator
* **Description**: Generates strong random passwords.
* **Flow**: Ask user how long they want the password to be. Use the `random` module to select letters and digits, combine them, and display the generated password.
