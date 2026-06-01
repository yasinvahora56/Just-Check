# Day 1: Introduction, Setup & Your First Program

Welcome to Day 1! Today is all about getting your development environment ready, understanding how Python runs under the hood, and writing your very first lines of code.

---

## Topics to Learn

### 1. What is Python & Where is it Used?
**Python** is a high-level, interpreted, general-purpose programming language. It was created by **Guido van Rossum** and first released in **1991**. Python is famous for its clean, easy-to-read syntax, which resembles plain English.

#### Where is Python Used?
* **Web Development**: Backend frameworks like Django and Flask.
* **Data Science & Machine Learning**: Analyzing data, building AI models (pandas, NumPy, TensorFlow, PyTorch).
* **Automation & Scripting**: Writing scripts to automate repetitive boring tasks.
* **Software Testing**: Automating testing processes (Selenium, PyTest).
* **Desktop & Game Development**: Basic games and GUI apps using Pygame or Tkinter.

#### Why Python is loved: Simplicity Comparison
Look at how much code is needed to just print **"Hello World"** in different languages:

##### Java:
```java
public class HelloWorld {
  public static void main(String[] args) {
    System.out.println("Hello World");
  }
}
```

##### Python:
```python
print("Hello World")
```
> **Notice the difference:** In Java, you need to worry about classes, methods, and access modifiers. In Python, a single line does it all! This makes Python extremely beginner-friendly.

---

### 2. Compiler vs. Interpreter (The Core Difference)
Computers cannot understand human-readable code directly; they only understand binary (`0`s and `1`s). We need a translator:

| Feature | Compiler (e.g., C, C++) | Interpreter (e.g., Python, JavaScript) |
| :--- | :--- | :--- |
| **Execution** | Translates the **entire** source code into machine code at once, creating an executable file (like `.exe`). | Translates and executes the code **line-by-line** at runtime. |
| **Speed** | Faster execution because it's pre-translated. | Slower execution as translation happens on-the-fly. |
| **Error Debugging** | Displays all errors only *after* scanning the entire program. | Stops execution the exact moment it hits an error, making debugging easier. |

> **How Python runs:** Python uses an **Interpreter**. When you run a Python file, the Python interpreter reads your code starting from line 1, runs it, then goes to line 2, and so on.

---

### 3. Introduction to VS Code
**Visual Studio Code (VS Code)** is a free, powerful, and lightweight Source Code Editor developed by Microsoft.
* **Why use it?** It supports syntax highlighting, auto-completions (IntelliSense), built-in terminal, and has an active ecosystem of extensions to make coding effortless.
* **Important Extensions**: Make sure to install the **Python** extension by Microsoft to enable running and debugging Python within VS Code.

---

### 4. Git & GitHub (Concept Only)
* **Git**: A software tool installed on your computer. It is a **Version Control System (VCS)** that keeps track of the history of changes you make to your files. If you break your code, Git lets you roll back to a working version.
* **GitHub**: A cloud-based website where developers host their Git repositories. It lets you share your code, collaborate with teams, and build a portfolio.
* **Analogical representation**: Think of **Git** as the camera taking snapshots of your project, and **GitHub** as the Instagram where you upload those snapshots to share with the world.

---

## Step-by-Step Installation Guides

### Step 1: Installing Python
1. **Download**: Go to the official website [python.org/downloads](https://www.python.org/downloads/) and click the yellow button to download the latest version for Windows.
2. **Run Installer**: Open the downloaded setup file.
3. ** CRITICAL STEP**: At the bottom of the installer window, check the box that says **"Add Python.exe to PATH"**. If you skip this, your terminal won't recognize python commands.
4. **Choose Install Now**: Click "Install Now" and wait for the process to complete.
5. **Verify**: Open your terminal (Command Prompt or PowerShell) and run:
  ```bash
  python --version
  ```
  *Expected Output: `Python 3.x.x` (where `x.x` is your installed version).*

---

### Step 2: Installing VS Code
1. Go to [code.visualstudio.com](https://code.visualstudio.com/) and download the Windows installer.
2. Run the installer, accept the agreement, and click **Next**.
3. **Recommended Settings**: Ensure the boxes for **"Add to PATH"** and **"Create a desktop icon"** are checked.
4. Open VS Code, click the **Extensions icon** on the left menu (four squares), search for `Python`, and click **Install** on the extension by Microsoft.

---

### Step 3: Installing Git
1. Go to [git-scm.com/downloads](https://git-scm.com/downloads) and download the Windows installer.
2. Run the setup, choose standard default options, and click install.
3. Once done, verify by opening Command Prompt and typing:
  ```bash
  git --version
  ```

---

### 5. The `print()` Function
In Python, the `print()` function is used to output messages or values to the screen.
* **Syntax**: `print("your message here")`
* Text messages (called **strings**) must be enclosed in quotes: `""` or `''`.
* Numbers and expressions do not need quotes: `print(5 + 5)` will output `10`.

---

## Practice Tasks
Let's apply what you learned! Navigate to the [tasks/](./tasks/) folder to complete today's assignments:
* [Task 1: Environment Setup](./tasks/task1_setup.md)
* [Task 2: First Programs](./tasks/task2_first_programs.py)
* [Task 3: Personal Info Program](./tasks/task3_personal_info.py)
* [Task 4: Debugging](./tasks/task4_debugging.py)
* [Task 5: Pattern Printing](./tasks/task5_pattern.py)
