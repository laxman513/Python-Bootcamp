import numpy as np

matrix = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("Matrix:")
print(matrix)

print("First row, first column:", matrix[0, 0])
print("Second row, third column:", matrix[1, 2])
print("Third row, second column:", matrix[2, 1])