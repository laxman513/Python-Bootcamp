import pandas as pd


data = {
    "Name": ["Rahul", "Priya", "Amit", "Sneha"],
    "Age": [25, 30, 35, 28],
    "Experience": [2, 5, 8, 4],
    "Salary": [50000, 70000, 90000, 65000]
}

df = pd.DataFrame(data)

print("First Row:")
print(df.iloc[0])

print("\nRows at positions 1 and 2:")
print(df.iloc[1:3])