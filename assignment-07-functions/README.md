# Assignment 7: Functions and Modules (CSC1015F)

## 📌 Overview
This assignment focused on transitioning from linear scripting to modular, reusable programming using **functions and modules**. Emphasizing a divide-and-conquer problem-solving strategy, the assignment required breaking complex tasks down into independent, testable functions, adhering to clean documentation, and ensuring compatibility with automated testing markers.

---

## 📁 Repository Structure & Program Details

### 🧮 Mathematical & Utility Functions
* **`cylinder.py`** *(Authored by me)*  
  Calculates the volume of a cylinder given its diameter and height. It implements a structured division of labor across three functions: `circle_area()`, `cylinder_volume()`, and `main()`.
* **`mymath.py`** *(Authored by me)*  
  A custom math module created by refactoring and adapting code from provided scripts. It contains required functions for integer input handling (`get_integer()`) and iterative factorial calculation (`calc_factorial()`).
* **`combine.py` / `fcombine.py`** *(Provided by UCT Department)*  
  Reference and testing programs provided to evaluate k-permutations of n items and assist in structuring modular mathematical utilities.

### 📊 Data Processing & Parsing
* **`extract.py`** *(Authored by me)*  
  A sensor data processing program that parses raw data streams containing blocks enclosed by `BEGIN` and `END` tags. It uses modular helper functions (`get_block()`, `location()`, `pressure()`, `temperature()`, `y_coordinate()`, and `x_coordinate()`) to extract, format, and display environmental metrics.

### 📅 Calendar Generation Program
* **`calendar_month.py`** *(Authored by me)*  
  Accepts a month name and year as input and prints out a neatly formatted calendar grid. It relies on a comprehensive set of modular functions—including `day_of_week()` (utilizing Zeller's congruence), `is_leap()`, `month_num()`, `num_days_in()`, `num_weeks()`, and `week()`—to calculate and assemble the calendar layout.

---

## 🛠️ Key Skills & Concepts Emphasized
* **Modular Design:** Breaking complex problems down into small, single-responsibility functions using a divide-and-conquer approach.
* **Scope & Reusability:** Designing functions with clear parameters and return values, and packaging functions into reusable custom modules.
* **Algorithmic Logic:** Implementing date algorithms (Zeller's congruence for day-of-week calculations), string parsing, and mathematical modeling.
* **Testing Compatibility:** Ensuring all modular scripts retained the standard execution guard (`if __name__=='__main__': main()`) to support individual function testing by automated markers.

---

## 🚀 How to Run
To run the interactive programs:
```bash
python3 cylinder.py
python3 extract.py
python3 calendar_month.py
