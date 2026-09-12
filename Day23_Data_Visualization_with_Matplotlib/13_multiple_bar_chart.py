import matplotlib.pyplot as plt
import numpy as np

departments = ["IT", "HR", "Finance", "Sales"]

salary_2025 = [70000, 55000, 65000, 60000]
salary_2026 = [80000, 60000, 75000, 68000]

x = np.arange(len(departments))

width = 0.35

plt.bar(
    x - width / 2,
    salary_2025,
    width,
    label="2025"
)

plt.bar(
    x + width / 2,
    salary_2026,
    width,
    label="2026"
)

plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.title("Average Salary Comparison")

# plt.xticks(x, departments)

plt.legend()

plt.show()