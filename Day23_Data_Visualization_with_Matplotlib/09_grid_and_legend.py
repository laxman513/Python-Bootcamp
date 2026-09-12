import matplotlib.pyplot as plt


months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]

product_a = [20, 25, 30, 28, 35, 40]
product_b = [15, 22, 27, 32, 34, 38]

plt.plot(
    months,
    product_a,
    marker="o",
    label="Product A"
)

plt.plot(
    months,
    product_b,
    marker="s",
    label="Product B"
)

plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Product Sales Comparison")

plt.legend()
plt.grid(True)

plt.show()