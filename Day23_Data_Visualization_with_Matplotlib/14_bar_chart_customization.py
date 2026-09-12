import matplotlib.pyplot as plt


departments = ["IT", "HR", "Finance", "Sales"]
employees = [40, 25, 20, 35]

bars = plt.bar(
    departments,
    employees,
    width=0.6
)

plt.xlabel("Department")
plt.ylabel("Number of Employees")
plt.title("Employee Count by Department")

plt.grid(
    axis="y",
    linestyle="--",
    alpha=0.5
)

# Display values on top of bars
for bar in bars:
    value = bar.get_height()

    plt.text(
        bar.get_x() + bar.get_width() / 2,
        value,
        str(value),
        ha="center",
        va="bottom"
    )

plt.show()