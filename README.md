# String Calculator

A Python implementation of the **String Calculator Kata**, built using **Test-Driven Development (TDD)** 

## Features

The String Calculator supports the following functionality:

1. **Basic Addition**:
   - Add up to two numbers separated by a comma (e.g., `"1,2"` returns `3`).
   - An empty string returns `0`.

2. **Handle Unknown Number of Inputs**:
   - Add an unknown number of numbers separated by commas (e.g., `"1,2,3,4"` returns `10`).

3. **Support for Newline as a Delimiter**:
   - Numbers can be separated by newlines (`\n`) in addition to commas (e.g., `"1\n2,3"` returns `6`).

4. **Custom Delimiters**:
   - Specify a custom delimiter at the beginning of the string using the format `//[delimiter]\n`.
   - Example: `"//;\n1;2;3"` returns `6`.

5. **Negative Number Validation**:
   - If the input contains negative numbers, an exception is raised with the message `"negatives not allowed"` followed by the list of negative numbers.
   - Example: `"1,-2,-3"` raises `ValueError: negatives not allowed: -2, -3`.

6. **Ignore Numbers Greater Than 1000**:
   - Numbers greater than `1000` are ignored in the sum (e.g., `"2,1001"` returns `2`).

7. **Delimiters of Any Length**:
   - Custom delimiters can be of any length when enclosed in square brackets.
   - Example: `"//[***]\n1***2***3"` returns `6`.

8. **Multiple Delimiters**:
   - Support for multiple custom delimiters, each enclosed in square brackets.
   - Example: `"//[*][%]\n1*2%3"` returns `6`.

9. **Multiple Delimiters with Variable Lengths**:
   - Delimiters of varying lengths are supported.
   - Example: `"//[***][%%]\n1***2%%3"` returns `6`.

---

## Prerequisites

- Python 3.8 or higher
- `pip` (Python package manager)

---

## Setup Instructions

Follow these steps to set up the project locally:

### 1. Clone the Repository

```bash
git clone https://github.com/swarnikaraj/tdd-kata.git
cd tdd-kata

### 2. Create a Virtual Environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

### 3. Install Dependencies
pip install -r requirements.txt

### 4. Run Tests
python -m pytest -v



<!-- Usage
You can use the StringCalculator class in your Python scripts. Here's an example: -->

from src.string_calculator import StringCalculator

calculator = StringCalculator()

# Basic addition
result = calculator.add("1,2")
print(result)  # Output: 3

# Custom delimiter
result = calculator.add("//[***]\n1***2***3")
print(result)  # Output: 6

# Negative number validation
try:
    result = calculator.add("1,-2,-3")
except ValueError as e:
    print(e)  # Output: negatives not allowed: -2, -3



## Project Structure

tdd-kata/
│
├── src/
│   └── string_calculator.py  # Main implementation of the String Calculator
│
├── tests/
│   └── test_string_calculator.py  # Test cases for the String Calculator
│
├── requirements.txt  # List of dependencies
├── README.md  # Project documentation
└── .gitignore  # Ignored files and directories