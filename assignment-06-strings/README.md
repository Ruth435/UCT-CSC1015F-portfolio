# Assignment 6: Strings (CSC1015F)

## 📌 Overview
This assignment focused heavily on **string manipulation and text processing** in Python. Building on basic input/output and control flow, it required mastering string indexing, slicing, concatenation, iteration, and core methods like `find()`, `strip()`, `int()`, and `str()` to parse and transform text data.

---

## 📁 Repository Structure & Program Details

* **`references.py`**  
  A bibliographic reference formatter that standardizes input references so that author names are formatted in title case and titles have only the first letter capitalized while preserving the rest of the metadata.

* **`convert.py`**  
  Converts a compact 24-hour date and time string (formatted as `yyyy-mm-dd hh:mm`) into an expanded 12-hour long-form representation (e.g., converting `2021-04-09 04:33` into `4:33 am on the 9th of April '21`), complete with appropriate ordinal day suffixes (`st`, `nd`, `rd`, `th`), am/pm handling, and two-digit year formatting.

* **`breakup.py`**  
  Takes an input sentence and tokenizes it into a comma-separated list of lowercase words ending with a full-stop, utilizing manual string parsing (`find()`) and loop logic without relying on built-in replacement methods.

* **`pig_latin.py`**  
  Translates an input sentence into a variant of Pig Latin. Words beginning with a vowel have "way" appended, while words beginning with consonants have their initial consonant sequence moved to the end, prefixed with "a" and followed by "ay".

---

## 🛠️ Key Skills & Concepts Emphasized
* **String Parsing & Slicing:** Extracting specific text segments using indexes, slices, and the `find()` method.
* **Text Formatting & Transformation:** Applying case changes, conditional suffix rules (for ordinals and dates), and tokenization.
* **Algorithmic Control Flow:** Using loops and conditional statements to parse strings character-by-character or word-by-word without advanced built-in shortcuts.

---

## 🚀 How to Run
To run any of the programs interactively:
```bash
python3 references.py
python3 convert.py
python3 breakup.py
python3 pig_latin.py
