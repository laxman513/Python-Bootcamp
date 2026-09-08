import numpy as np

employees = np.array([
    [25, 2, 50000],
    [30, 5, 70000],
    [35, 8, 90000],
    [40, 12, 120000]
])

print("Employee data:")
print(employees)

print()
print("Shape:", employees.shape)

ages = employees[:, 0]
experience = employees[:, 1]
salary = employees[:, 2]

print()
print("Ages:", ages)
print("Experience:", experience)
print("Salary:", salary)

print()
print("Average age:", np.mean(ages))
print("Average experience:", np.mean(experience))
print("Average salary:", np.mean(salary))