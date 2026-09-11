import pandas as pd

marks = pd.Series([85, 78, 92, 88, 76])

print("Marks:")
print(marks)

print("\nFirst Mark:", marks[0])
print("Thrid Mark:", marks[2])

print("\nSeries values:")
print(marks.values)

print("\nSeries indexs:")
print(marks.index)