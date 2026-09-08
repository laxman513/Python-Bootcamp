import numpy as np


employees = np.array([
    [101, 25, 2, 50000],
    [102, 30, 5, 70000],
    [103, 35, 8, 90000],
    [104, 40, 12, 120000],
    [105, 28, 4, 65000]
])

ages = employees[:, 1]
experience = employees[:, 2]
salaries = employees[:, 3]

print("Average age:", np.mean(ages))
print("Average age:", np.mean(ages))
print("Average age:", np.mean(ages))

print("Minimum salary:", np.min(salaries))
print("Maximum salary:", np.max(salaries))

high_salary_employees = employees[employees[:, 3] > 70000]
print("\nEmployees With Salary Greater Than 70000:")
print(high_salary_employees)

