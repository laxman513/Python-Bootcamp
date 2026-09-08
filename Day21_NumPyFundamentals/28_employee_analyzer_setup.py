import numpy as np

employees = np.array([
    [101, 25, 2, 50000],
    [102, 30, 5, 70000],
    [103, 35, 8, 90000],
    [104, 40, 12, 120000],
    [105, 28, 4, 65000]
])

print("Employee Dataset:")
print(employees)

print("\nShape:", employees.shape)
print("Number of Employees:", employees.shape[0])
print("Number of Columns:", employees.shape[1])

print("\nEmployee Id's:", employees[:, 0])
print("Ages:", employees[:, 1])
print("Experience: ", employees[:, 2])
print("Salaries: ", employees[:, 3])
