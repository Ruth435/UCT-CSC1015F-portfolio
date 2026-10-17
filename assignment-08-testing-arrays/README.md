# Assignment 8: Testing and Arrays (CSC1015F)

## 📌 Overview
This assignment focused on two core areas of software engineering: rigorous software testing using Python's doctest module (aiming for statement and path coverage) and array/list data manipulation through modular programs handling 2D grids, vector mathematics, and frequency histograms.

---

## 📁 Repository Structure & Program Details

### 🧪 Testing Modules & Provided Code
* **`testnumberutil.py`** *(Authored by me)*  
  A doctest script containing 8 test cases designed to achieve full path coverage for the `numberutil.aswords()` function (converting integers 0 to 999 into their English language equivalents)[cite: 1].
* **`numberutil.py`** *(Provided by UCT Department)*  
  The base module containing the `aswords()` function supplied for testing[cite: 1].
* **`testpalindrome.py`** *(Authored by me)*  
  A doctest script containing 5 test cases designed to achieve statement coverage for the `palindrome.is_palindrome()` function, accounting for spacing and case-sensitivity rules[cite: 1].
* **`palindrome.py`** *(Provided by UCT Department)*  
  The base module containing the `is_palindrome()` function supplied for testing[cite: 1].

### 💻 Array & Data Processing Programs (Authored by me)
* **`gridio.py`**  
  Allows a user to input and query a 2-dimensional 9 x 9 grid using space-separated integer coordinates (x, y), continuing until -1 -1 is entered to terminate[cite: 1].
* **`vectormath.py`**  
  A menu-driven program for 2D and 3D vector calculations. Supports magnitude computation, vector addition, scalar multiplication, dot products, and 3-dimensional cross products with validation for vector lengths[cite: 1].
* **`histogram.py`**  
  Takes a space-separated list of student marks, categorizes them according to standard UCT grading bands (Fail, 3rd, Lower 2nd, Upper 2nd, First), and prints a horizontal ASCII bar chart using X characters[cite: 1].

---

## 🛠️ Key Skills & Concepts Emphasized
* **Test-Driven Principles:** Writing modular doctest suites (`doctest.testmod(verbose=True)`) to verify statement and path coverage[cite: 1].
* **Data Structures:** Working extensively with lists, 2D arrays, and dictionaries[cite: 1].
* **Algorithm Design:** Implementing mathematical formulas (vector arithmetic, cross products) and frequency counting logic[cite: 1].
* **Code Quality:** Maintaining clean documentation, meaningful identifiers, and robust input parsing[cite: 1].

---

## 🚀 How to Run
To execute the doctest files:
```bash
python3 testnumberutil.py
python3 testpalindrome.py
