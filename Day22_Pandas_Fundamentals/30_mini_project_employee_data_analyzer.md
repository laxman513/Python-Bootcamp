# Program 30 — Employee Data Analyzer

## Objective

Build a complete Pandas-based Employee Data Analyzer.

## Features

1. Load employee data from CSV
2. Display dataset information
3. Detect missing values
4. Clean missing values
5. Calculate employee statistics
6. Create experience categories
7. Create salary categories
8. Analyze departments
9. Find high earners
10. Find top employees
11. Sort employees by salary
12. Save the final analyzed dataset

## Pandas Concepts Used

- read_csv()
- DataFrame
- shape
- columns
- isna()
- fillna()
- mean()
- min()
- max()
- np.where()
- query()
- groupby()
- agg()
- reset_index()
- sort_values()
- head()
- to_csv()

## Input

data/employees.csv

## Output

data/employee_analysis_report.csv

## Run

python 30_employee_data_analyzer.py

## Final Verification

The program should:

- Load the CSV
- Detect missing values
- Clean the data
- Add Experience_Level
- Add Salary_Category
- Display statistics
- Display department summary
- Display high earners
- Display top employees
- Create employee_analysis_report.csv