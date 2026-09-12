import matplotlib.pyplot as plt


x = [1, 2, 3, 4, 5]

actual = [10, 15, 13, 20, 25]
target = [12, 16, 18, 22, 28]

plt.plot(
    x,
    actual,
    marker="o",
    linestyle="-",
    label="Actual"
)

plt.plot(
    x,
    target,
    marker="o",
    linestyle="--",
    label="Target"
)

plt.xlabel("Month")
plt.ylabel("Value")
plt.title("Actual vs Target")

plt.legend()
plt.grid(True)

plt.show()