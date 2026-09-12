import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5, 6, 7]
sales = [20, 25, 22, 30, 35, 32, 40]

plt.plot(
    days, 
    sales,
    marker="o",
    linestyle="--",
    linewidth=2
)

plt.xlabel("Days")
plt.ylabel("Sales")
plt.title("Weekly Sales")

plt.grid(True)

plt.show()
