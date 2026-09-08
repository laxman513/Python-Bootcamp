import numpy as np

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print("Original matrix:", matrix)
print("Original shape:", matrix.shape)

transpose = np.transpose(matrix)

print("Transpose:", transpose)
print("Transposed shape:", transpose.shape)

transpose2 = matrix.T

print("Transpose2:", transpose2)
print("Transposed2 shape:", transpose2.shape)