import numpy as np

array_1d = np.array([10, 20, 30, 40])

array_2d = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

array_3d = np.array([
    [
        [1, 2],
        [3, 4]
    ],
    [
        [5, 6],
        [7, 8]
    ]
])

array_4d = np.array([
    [
        [
            [1, 2],
            [2, 3]
        ],
        [
            [1, 2],
            [2, 3]
        ]
    ],
    [
        [
            [1, 2],
            [2, 3]
        ],
        [
            [1, 2],
            [2, 3]
        ]
    ]
])

print("1D array:")
print(array_1d)
print("Dimensions:", array_1d.ndim)

print()

print("2D array:")
print(array_2d)
print("Dimensions:", array_2d.ndim)

print()

print("3D array:")
print(array_3d)
print("Dimensions:", array_3d.ndim)

print("4D array:")
print(array_4d)
print("Dimensions:", array_4d.ndim)