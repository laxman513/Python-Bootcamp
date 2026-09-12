import matplotlib.pyplot as plt

experience = [2, 3, 5, 7, 8, 10, 12]

salary = [45000, 50000, 60000, 70000, 80000, 95000, 120000]

plt.scatter(experience, salary)

plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.title("Experience vs Salary")

plt.grid(True)

plt.show()