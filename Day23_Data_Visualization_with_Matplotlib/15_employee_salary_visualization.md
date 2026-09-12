# Program 15 — Employee Salary Visualization

## Objective

Combine Pandas and Matplotlib to visualize employee salaries.

## Input

Day22 employee dataset:

../Day22_Pandas/data/employees.csv

## Steps

1. Load CSV using Pandas
2. Handle missing Salary values
3. Sort employees by Salary
4. Create a bar chart
5. Display employee names
6. Display salaries

## Concepts Used

### Pandas

- read_csv()
- fillna()
- sort_values()

### Matplotlib

- plt.bar()
- xlabel()
- ylabel()
- title()
- xticks()
- tight_layout()
- show()

## Run

python 15_employee_salary_visualization.py

## Expected Result

A bar chart showing each employee and their salary.

Employees should be arranged from highest salary to lowest salary.