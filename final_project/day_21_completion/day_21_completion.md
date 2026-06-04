# Day 21: Project Completion, Debugging & Presentation

Welcome to Day 21! Today is the final day of the internship course. 

You have a working base project from Day 20. Today, you will polish it, fix any hidden bugs, make the output look professional, and finally, present it!

---

## 1. Debugging and Edge Cases

Your code might work when you enter perfectly valid data, but what if the user makes a mistake? A robust app handles "edge cases" gracefully.

**Common Edge Cases to test:**
*   What happens if the user enters letters when asked for an amount? (Handled via `try-except ValueError`)
*   What happens if they try to view expenses when the JSON file is empty or missing? (Check if list is empty before printing)
*   What happens if they enter a negative number for an expense? (Add a check `if amount < 0: print("Invalid")`)

---

## 2. Feature Enhancement (Improving UX)

User Experience (UX) is critical. Your app should be a joy to use.

*   **Better Formatting:** Use f-strings to format currency to two decimal places (`${amount:.2f}`). Use `---` or `=` to separate sections clearly.
*   **Input Validation:** Use `while` loops to keep asking for input until the user provides something valid, rather than just printing an error and returning to the main menu.
*   **Extra Features:** (e.g., allow the user to delete a specific expense, or sort expenses by category).

---

## 3. Code Cleanup (Refactoring)

Before presenting, clean up your code.
*   **Proper Naming:** Ensure variables are descriptive (`expense_amount` instead of just `x` or `a`).
*   **Remove Duplicates:** If you have the exact same 5 lines of code in two different places, move them into a single helper function.
*   **Add Comments:** Briefly explain complex logic.

---

## 4. Presentation Requirements

You will present your final project. Be prepared to:
1.  **Introduce your app**: What does it do?
2.  **Show a live demo**: Run the code, add some data, view it, and show what happens when you type bad input.
3.  **Explain the code logic**: Show your JSON saving/loading logic and explain how your main loop works.

---

## Practice Tasks
Navigate to the [tasks/](./tasks/) folder to complete today's assignments. 

*These tasks will guide you through polishing the Expense Tracker.*

* [Task 1: Debugging](./tasks/task1_debugging.py)
* [Task 2: Feature Enhancement](./tasks/task2_enhancement.py)
* [Task 3: Final Output Improvement](./tasks/task3_output_improvement.py)
* [Task 4: Code Cleanup](./tasks/task4_code_cleanup.py)
* [Task 5: Final Finished Project](./tasks/task5_final_project.py)
