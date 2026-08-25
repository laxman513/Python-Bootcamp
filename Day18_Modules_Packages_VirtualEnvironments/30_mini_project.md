# Program 30 — Day 18 Mini Project

## Project Name

Student Information Manager

---

## Objective

Build a small Python project that combines the concepts learned in Day 18.

The project demonstrates:

1. Modules
2. Packages
3. Functions
4. Imports
5. Third-party packages
6. Virtual environment
7. Requirements file
8. main() function
9. __name__ == "__main__"

---

# Project Structure

Day18_Modules_Packages_VirtualEnvironments/
│
├── 30_mini_project.md
├── 30_student_manager.py
│
└── student_utils/
    ├── __init__.py
    └── student.py

---

# Step 1 — Create the package

Create a folder:

student_utils

Inside the folder create:

__init__.py

and:

student.py

The student_utils folder is a Python package.

---

# Step 2 — Create the student module

student.py will contain functions related to student information.

Functions:

1. calculate_average()
2. get_result()

The module should contain only student-related functionality.

---

# Step 3 — Create the main program

Create:

30_student_manager.py

The main program should:

1. Import functions from student_utils.student.
2. Define student information.
3. Calculate the average marks.
4. Determine PASS or FAIL.
5. Display the student information.
6. Use the requests package.
7. Display the HTTP status code.
8. Use a main() function.
9. Use the __name__ == "__main__" guard.

---

# Step 4 — Use the virtual environment

The program must run using the .venv virtual environment.

Activate it using PowerShell:

.venv\Scripts\Activate.ps1

The terminal should display:

(.venv)

---

# Step 5 — Third-party package

The project uses:

requests

The requests package must be installed inside .venv.

Verify:

pip show requests

---

# Step 6 — Requirements file

The dependencies for this Day 18 environment are recorded in:

29_requirements.txt

The file contains packages such as:

requests
certifi
charset-normalizer
idna
urllib3

with their versions.

---

# Step 7 — Expected project flow

30_student_manager.py
        |
        ↓
student_utils package
        |
        ↓
student.py
        |
        ├── calculate_average()
        |
        └── get_result()
        |
        ↓
Display student result
        |
        ↓
requests package
        |
        ↓
Display HTTP status

---

# Step 8 — Example student data

Example:

Name:

Rahul

Marks:

85, 78, 92

Average:

85.0

Result:

PASS

---

# Step 9 — Expected output

Example:

Student Name: Rahul
Marks: [85, 78, 92]
Average: 85.0
Result: PASS
Internet Status: 200

The actual values can be different.

---

# Concepts Demonstrated

## Module

student.py

## Package

student_utils/

## Package initialization

__init__.py

## Import

from student_utils.student import calculate_average, get_result

## Third-party package

requests

## Virtual environment

.venv

## Dependency file

29_requirements.txt

## Main function

def main():

## Main guard

if __name__ == "__main__":
    main()

---

# Important Learning Point

A professional Python project is usually divided into multiple modules and packages instead of putting everything into one large Python file.

Virtual environments isolate project dependencies.

Requirements files record the dependencies needed by a project.

---

# Program 30 Checklist

[ ] Create student_utils folder

[ ] Create __init__.py

[ ] Create student.py

[ ] Create 30_student_manager.py

[ ] Create calculate_average()

[ ] Create get_result()

[ ] Import functions from student_utils.student

[ ] Define student information

[ ] Calculate average marks

[ ] Determine PASS/FAIL

[ ] Import requests

[ ] Make a requests call

[ ] Display HTTP status code

[ ] Use main()

[ ] Use __name__ == "__main__"

[ ] Run inside .venv

[ ] Verify successful output

[ ] Day 18 completed