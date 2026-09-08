import numpy as np

numbers = np.arange(1, 7)

print("Original array:", numbers)

print("Original shape:", numbers.shape)

matrix = numbers.reshape(2, 3)

print()
print("Reshaped array:")
print(matrix)

print("New shape:", matrix.shape)