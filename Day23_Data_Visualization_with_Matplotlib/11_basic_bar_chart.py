import matplotlib.pyplot as plt

departments = ["IT", "HR", "Finance", "Sales"]
employees = [40, 25, 20, 35]

plt.bar(departments, employees)

plt.xlabel("Department")
plt.ylabel("Number of Employees")
plt.title("Employees by Department")

plt.show()