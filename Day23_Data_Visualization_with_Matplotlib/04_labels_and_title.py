import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5, 6, 7]
sales = [20, 25, 22, 30, 35, 32, 40]

plt.plot(days, sales)

plt.xlabel("Days")
plt.ylabel("Sales")
plt.title("Weekly Sales")

plt.show()
