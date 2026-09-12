import matplotlib.pyplot as plt


# Data
months = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
]

sales = [
    100,
    120,
    115,
    140,
    160,
]


departments = [
    "IT",
    "HR",
    "Finance",
    "Sales",
]

employees = [
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


plt.figure(figsize=(12, 8))


# Line chart
plt.subplot(2, 2, 1)

plt.plot(months, sales, marker="o")

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True)


# Bar chart
plt.subplot(2, 2, 2)

plt.bar(departments, employees)

plt.title("Employees by Department")
plt.xlabel("Department")
plt.ylabel("Employees")


# Scatter plot
plt.subplot(2, 2, 3)

plt.scatter(experience, salary)

plt.title("Experience vs Salary")
plt.xlabel("Experience")
plt.ylabel("Salary")
plt.grid(True)


# Histogram
plt.subplot(2, 2, 4)

plt.hist(salary, bins=5)

plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Frequency")


plt.tight_layout()

plt.show()