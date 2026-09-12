import matplotlib.pyplot as plt


months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [20, 25, 30, 28, 35, 40]

plt.plot(
    months,
    sales,
    marker="o"
)

plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Monthly Sales")

plt.grid(True)

plt.show()