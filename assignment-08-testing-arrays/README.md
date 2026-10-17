# Assignment 8: Testing and Arrays (CSC1015F)

## 📌 Overview
This assignment focused on two core areas of software engineering: rigorous software testing using Python's doctest module (aiming for statement and path coverage) and array/list data manipulation through modular programs handling 2D grids, vector mathematics, and frequency histograms.

---

## 📁 Repository Structure & Program Details

### 🧪 Testing Modules
* **`testnumberutil.py`**  
  A doctest script containing 8 test cases designed to achieve full path coverage for the `numberutil.aswords()` function (converting integers 0 to 999 into their English language equivalents).
* **`testpalindrome.py`**  
  A doctest script containing 5 test cases designed to achieve statement coverage for the `palindrome.is_palindrome()` function, accounting for spacing and case-sensitivity rules.

### 💻 Array & Data Processing Programs
* **`gridio.py`**  
  Allows a user to input and query a 2-dimensional 9 x 9 grid using space-separated integer coordinates (x, y), continuing until -1 -1 is entered to terminate.
* **`vectormath.py`**  
  A menu-driven program for 2D and 3D vector calculations. Supports magnitude computation, vector addition, scalar multiplication, dot products, and 3-dimensional cross products with validation for vector lengths.
* **`histogram.py`**  
  Takes a space-separated list of student marks, categorizes them according to standard UCT grading bands (Fail, 3rd, Lower 2nd, Upper 2nd, First), and prints a horizontal ASCII bar chart using X characters.

---

## 🛠️ Key Skills & Concepts Emphasized
* **Test-Driven Principles:** Writing modular doctest suites (`doctest.testmod(verbose=True)`) to verify statement and path coverage.
* **Data Structures:** Working extensively with lists, 2D arrays, and dictionaries.
* **Algorithm Design:** Implementing mathematical formulas (vector arithmetic, cross products) and frequency counting logic.
* **Code Quality:** Maintaining clean documentation, meaningful identifiers, and robust input parsing.

---

## 🚀 How to Run
To execute the doctest files:
```bash
python3 testnumberutil.py
python3 testpalindrome.py
