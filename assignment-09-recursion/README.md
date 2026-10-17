# Assignment 9: Recursion (CSC1015F)

## 📌 Overview
This assignment focused entirely on mastering **recursive programming concepts** in Python. A strict constraint of this assignment was the complete prohibition of iterative constructs (such as `for` and `while` loops) as well as standard string/list reversal shortcuts, requiring all logic to be solved through pure recursion.

---

## 📁 Repository Structure & Program Details

* **`pairs.py`**  
  Contains a recursive function that counts the number of non-overlapping consecutive character pairs within a given string input.

* **`encrypt.py`**  
  Implements a recursive text encryption function that shifts all lowercase alphabetical characters to the next character in sequence (with a wrap-around from `z` to `a`), leaving other characters unaffected.

* **`palindromeprimes.py`**  
  Finds all palindromic prime numbers within a specified range from $N$ to $M$ (inclusive) using recursive helper functions. It integrates core recursive palindrome-checking logic and requires an expanded Python system recursion limit (`sys.setrecursionlimit`).

---

## 🛠️ Key Constraints & Skills Emphasized
* **Pure Recursion:** Solving complex string processing, pattern matching, and mathematical search routines without loops.
* **Algorithmic Efficiency:** Designing clean base cases and recursive steps to prevent stack overflows.
* **Documentation & Style:** Adhering to clean code standards, including module-level docstrings, inline comments for non-obvious logic, and meaningful variable naming.

---

## 🚀 How to Run
To run any of the programs interactively:
```bash
python3 pairs.py
python3 encrypt.py
python3 palindromeprimes.py
