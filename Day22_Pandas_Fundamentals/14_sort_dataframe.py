import pandas as pd


df = pd.DataFrame({
    "Name": ["Rahul", "Priya", "Amit", "Sneha"],
    "Age": [25, 30, 35, 28],
    "Salary": [50000, 70000, 90000, 65000]
})

print("Original DataFrame:")
print(df)

print("\nSalary - Low to High:")
print(df.sort_values("Salary"))

print("\nSalary - High to Low:")
print(df.sort_values("Salary", ascending=False))