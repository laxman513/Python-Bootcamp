import matplotlib.pyplot as plt


months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]

sales = [20, 25, 30, 28, 35, 40]
expenses = [10, 15, 18, 17, 20, 22]


plt.figure(figsize=(10, 6))


# First subplot
plt.subplot(2, 1, 1)

plt.plot(
    months,
    sales,
    marker="o"
)

plt.title("Monthly Sales")
plt.ylabel("Sales")
plt.grid(True)


# Second subplot
plt.subplot(2, 1, 2)

plt.plot(
    months,
    expenses,
    marker="s"
)

plt.title("Monthly Expenses")
plt.xlabel("Month")
plt.ylabel("Expenses")
plt.grid(True)


plt.tight_layout()

plt.show()