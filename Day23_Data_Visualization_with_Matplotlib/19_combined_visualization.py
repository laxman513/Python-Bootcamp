import matplotlib.pyplot as plt


departments = [
    "IT",
    "HR",
    "Finance",
    "Sales",
]

employee_count = [
    40,
    20,
    15,
    25,
]

experience = [
    2,
    3,
    5,
    7,
    8,
    10,
    12,
]

salary = [
    45000,
    50000,
    60000,
    70000,
    80000,
    95000,
    120000,
]

salaries = [
    45000,
    50000,
    55000,
    60000,
    65000,
    70000,
    75000,
    80000,
    85000,
    90000,
    95000,
    100000,
    110000,
    120000,
]

plt.figure(figsize=(12, 8))

#1 Dar Chart
plt.subplot(2, 2, 1)

plt.bar(departments, employee_count)

plt.title("Employees by Department")
plt.xlabel("Department")
plt.ylabel("Employees")

#2 Scatter plot
plt.subplot(2, 2, 2)

plt.scatter(experience, salary)

plt.title("Experience vs Salary")
plt.xlabel("Experience")
plt.ylabel("Salary")

# 3. Histogram
plt.subplot(2, 2, 3)

plt.hist(salaries, bins=5)

plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Frequency")


plt.tight_layout()

plt.show()