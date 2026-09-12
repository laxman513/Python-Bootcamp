import matplotlib.pyplot as plt


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


plt.hist(salaries, bins=5)

plt.xlabel("Salary")
plt.ylabel("Number of Employees")
plt.title("Employee Salary Distribution")

plt.grid(True)

plt.show()