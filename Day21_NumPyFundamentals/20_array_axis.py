import numpy as np

marks = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print("Marks:")
print(marks)

print()

print("Total number of marks:", np.sum(marks))

print("Columns totals:", np.sum(marks, axis=0))

print("Rows Totals:", np.sum(marks, axis=1))

# print("Rows Totals:", np.sum(marks, axis=2))