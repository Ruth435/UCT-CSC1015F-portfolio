# Assignment 5: Control Structures (CSC1015F)

## 📌 Overview
This assignment focused heavily on control flow mechanisms in Python—specifically utilizing `if` and `if-else` conditional statements, `while` loops, and nested `for` loops—combined with numerical manipulation to build grid layouts, calendar generators, and menu-driven command loops.

---

## 📁 Repository Structure & Program Details

* **`grid.py`**  
  Accepts a starting number `n` (within the strict range between -6 and 2) and prints a sequence of 42 numbers arranged in 6 rows of 7 numbers each. It includes input validation for out-of-range values and formats the output using right-justified field widths separated by spaces.

* **`printmonth.py`**  
  Asks the user for a month name and a starting day (1 for Monday through 7 for Sunday), then generates and prints a calendar grid spanning 6 rows by 7 columns. It includes validation checks for invalid month names or start days, and handles standard month lengths (treating February as 28 days).

* **`bulletin.py`**  
  Simulates a classic public Bulletin Board System (BBS) menu interface. It runs in a continuous loop allowing users to enter a message, view the stored message (defaulting to "no message yet"), list available files (`42.txt`, `1015.txt`), display file contents, or exit the program safely.

---

## 🛠️ Key Skills & Concepts Emphasized
* **Control Flow:** Implementing complex branching logic with `if`, `elif`, and `else` statements.
* **Iteration:** Using nested `for` loops and continuous `while` loops to manage menu states and multi-row grid formatting.
* **Input Validation:** Checking user inputs against valid ranges and parameters, and handling errors gracefully.
* **Text Formatting:** Aligning text and numbers into strict tabular and grid structures for terminal outputs.

---

## 🚀 How to Run
To run any of the programs interactively:
```bash
python3 grid.py
python3 printmonth.py
python3 bulletin.py
