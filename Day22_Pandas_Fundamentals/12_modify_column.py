import pandas as pd

data = {
    "Name": ["Rahul", "Priya", "Amit", "Sneha"],
    "Age": [25, 30, 35, 28],
    "Experience": [2, 5, 8, 4],
    "Salary": [50000, 70000, 90000, 65000]
}

df = pd.DataFrame(data)

print("Before Salary Revision:")
print(df)

df["Salary"] = df["Salary"] * 1.10

print("\nAfter 10% Salary Revision:")
print(df)