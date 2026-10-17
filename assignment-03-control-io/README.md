# Assignment 3: Console Input/Output and Control (CSC1015F)

## 📌 Overview
This assignment focused on foundational Python input and output operations, basic formatting parameters (`sep`, `end`), conditional control flow (`if` and `if-else`), escape characters, and numerical problem-solving like Heron's triangle area formula and calendar leap year calculations.

---

## 📁 Repository Structure & Program Details

* **`triangle.py`**  
  Asks the user to enter the lengths of the three sides of a triangle, calculates its area using Heron's formula (incorporating the math module for square roots), validates whether the inputs form a valid triangle, and prints the result rounded to two decimal places.

* **`rabbit.py`**  
  A creative ASCII art program that uses print statements and properly escaped backslashes to render a detailed multi-character rabbit graphic in the terminal console.

* **`spam.py`**  
  Generates a humorous, personalized spam message template based on user inputs for first name, last name, a sum of money in USD, and country name, calculating a 30% payout share and formatting names dynamically.

* **`leapYear.py`**  
  Accepts an integer representing a year and determines whether it is a leap year based on standard calendar rules (divisible by 400, or divisible by 4 but not by 100).

* **`time.py`**  
  Validates an entered time by checking whether hours (0-23), minutes (0-59), and seconds (0-59) fall within valid inclusive numerical ranges.

---

## 🛠️ Key Skills & Concepts Emphasized
* **Console I/O:** Handling user inputs, casting data types, and mastering print formatting options (`sep`, `end`, escape characters like `\n` and `\\`).
* **Conditional Logic:** Implementing multi-condition checks (`if`, `elif`, `else`) for data validation and leap year/triangle feasibility rules.
* **Mathematical Operations:** Using library modules (`math.sqrt`) and arithmetic formulas to solve geometry and time constraints.

---

## 🚀 How to Run
To run any of the programs interactively:
```bash
python3 triangle.py
python3 rabbit.py
python3 spam.py
python3 leapYear.py
python3 time.py
