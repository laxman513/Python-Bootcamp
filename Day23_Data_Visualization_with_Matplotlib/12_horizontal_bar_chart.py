import matplotlib.pyplot as plt


departments = [
    "Information Technology",
    "Human Resources",
    "Finance",
    "Customer Support"
]

employees = [40, 25, 20, 35]

plt.barh(departments, employees)

plt.xlabel("Number of Employees")
plt.ylabel("Department")
plt.title("Employees by Department")

plt.show()