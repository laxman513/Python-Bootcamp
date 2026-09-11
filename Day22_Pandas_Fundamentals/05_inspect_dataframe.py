import pandas as pd


data = {
    "Name": ["Rahul", "Priya", "Amit", "Sneha"],
    "Age": [25, 30, 35, 28],
    "Experience": [2, 5, 8, 4],
    "Salary": [50000, 70000, 90000, 65000]
}

df = pd.DataFrame(data)

print("DataFrame:")
print(df)

print("\nShape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nValues:")
print(df.values)

print("\nData Types:")
print(df.dtypes)

print("\nFirst 2 rows")
print(df.head(2))

print("\nLast 2 rows")
print(df.tail(2))