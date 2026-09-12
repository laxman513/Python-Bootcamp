import matplotlib.pylab as plt

departments = [
    "IT",
    "HR",
    "Finance",
    "Sales"
]

employees = [
    40,
    20,
    15,
    25
]

plt.pie(
    employees,
    labels=departments,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Employee Distribution by Department")

plt.show()