import numpy as np

numbers = np.arange(1, 7)

print("Original array:")
print(numbers)

matrix1 = numbers.reshape(2, -1)

print()
print("reshape(2, -1):")
print(matrix1)
print("Shape:", matrix1.shape)

matrix2 = numbers.reshape(3, -1)

print()
print("reshape(3, -1):")
print(matrix2)
print("Shape:", matrix2.shape)

matrix3 = numbers.reshape(-1, 1)

print()
print("reshape(-1, 1):")
print(matrix3)
print("Shape:", matrix3.shape)