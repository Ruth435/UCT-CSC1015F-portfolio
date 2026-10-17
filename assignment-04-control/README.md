# Assignment 4: Control Structures and Number Theory (CSC1015F)

## 📌 Overview
This assignment focused on expanding control flow logic using conditional statements (`if`, `elif`, `else`) and `for` loops, alongside numerical manipulation. It covers implementing a simple expert system decision tree, analyzing number theory properties (proper divisors and perfect numbers), and formatting sequential number outputs into rows and columns.

---

## 📁 Repository Structure & Program Details

* **`cupcake.py`**  
  A rule-based expert system (decision tree) that prompts the user through a series of yes/no questions to determine whether dropped food (like a cupcake) is safe to eat according to the classic "30-second rule" logic.

* **`perfect.py`**  
  Determines whether a given positive integer is a "perfect number" (a number equal to the sum of its proper divisors). It identifies and prints all proper divisors of the number followed by a confirmation statement.

* **`row.py`**  
  Asks the user to enter a starting number `n` (where -6 < n < 93) and prints a sequence of 7 consecutive numbers starting from `n`. Each number is formatted with a right-justified field width of 2, padding single-digit numbers with a leading space.

* **`column.py`**  
  Asks the user to enter a starting number `n` (where -6 < n < 2) and prints every 7th number in the range from `n` to `n + 41`, with each number appearing on a new line and right-justified using a field width of 2.

---

## 🛠️ Key Skills & Concepts Emphasized
* **Decision Trees & Branching:** Using nested conditional statements (`if-else`) to navigate logic paths based on user inputs.
* **Number Theory:** Computing mathematical factors, proper divisors, and sums to evaluate number properties.
* **Formatted Output:** Controlling spacing, alignments, and field widths for text-based terminal layouts.
* **Iteration:** Generating number ranges and stepping through sequences using loops.

---

## 🚀 How to Run
To run any of the programs interactively:
```bash
python3 cupcake.py
python3 perfect.py
python3 row.py
python3 column.py
