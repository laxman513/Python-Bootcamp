import pandas as pd


df = pd.DataFrame({
    "Name": [
        "Rahul", "Priya", "Amit",
        "Sneha", "Kiran", "Vijay"
    ],
    "Department": [
        "IT", "HR", "IT",
        "HR", "IT", "Finance"
    ],
    "Salary": [
        50000, 60000, 90000,
        65000, 120000, 70000
    ]
})

print("Employee Data:")
print(df)

print("\nAverage Salary by Department:")
print(df.groupby("Department")["Salary"].mean())

print("\nTotal Salary by Department:")
print(df.groupby("Department")["Salary"].sum())