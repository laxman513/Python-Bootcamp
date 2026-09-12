import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]

sales_2025 = [20, 25, 30, 28, 35, 40]
sales_2026 = [25, 28, 32, 35, 38, 45]

plt.plot(months, sales_2025, label="2025")
plt.plot(months, sales_2026, label="2026")

plt.xlabel("Months")
plt.ylabel("Sales")
plt.title("Sales Comparison: 2025 vs 2026")

plt.legend()

plt.grid(True)

plt.show()