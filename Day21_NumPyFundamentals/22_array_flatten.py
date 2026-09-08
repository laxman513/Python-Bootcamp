import numpy as np

matrix = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print("Original matrix:")
print(matrix)

print("Original shape:", matrix.shape)

flattened = matrix.flatten()

print()
print("Flattened array:")
print(flattened)