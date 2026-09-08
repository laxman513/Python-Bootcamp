import numpy as np

salaries = np.array([
    50000,
    65000,
    72000,
    48000,
    90000,
    85000
])

print("Salaries:", salaries)

average_salary = np.mean(salaries)

minimum_salary = np.min(salaries)

maximum_salary = np.max(salaries)

high_salaries = salaries[salaries > 70000]

print("Average Salary:", average_salary)
print("Minimum Salary:", minimum_salary)
print("Maximum Salary:", maximum_salary)
print("Salaries Greater Than 70000:", high_salaries)
print("Number of Employees Above 70000:", high_salaries.size)
