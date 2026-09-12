from pathlib import Path

import pandas as pd

# --------------------------------------------------
# Create data directory
# --------------------------------------------------
DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)

# --------------------------------------------------
# CSV file path
# --------------------------------------------------

FILE_PATH = DATA_DIR / "employees.csv"

# --------------------------------------------------
# Employee dataset
# --------------------------------------------------

employees = [
    {
        "Employee_ID": 101,
        "Name": "Rahul",
        "Department": "IT",
        "Age": 25,
        "Experience": 2,
        "Salary": 50000,
    },
    {
        "Employee_ID": 102,
        "Name": "Priya",
        "Department": "HR",
        "Age": 30,
        "Experience": 5,
        "Salary": 70000,
    },
    {
        "Employee_ID": 103,
        "Name": "Amit",
        "Department": "Finance",
        "Age": 35,
        "Experience": 8,
        "Salary": 90000,
    },
    {
        "Employee_ID": 104,
        "Name": "Sneha",
        "Department": "IT",
        "Age": 40,
        "Experience": 12,
        "Salary": 120000,
    },
    {
        "Employee_ID": 105,
        "Name": "Kiran",
        "Department": "Sales",
        "Age": 28,
        "Experience": 4,
        "Salary": 60000,
    },
    {
        "Employee_ID": 106,
        "Name": "Anjali",
        "Department": "Finance",
        "Age": 32,
        "Experience": 7,
        "Salary": 85000,
    },
    {
        "Employee_ID": 107,
        "Name": "Vikram",
        "Department": "IT",
        "Age": 45,
        "Experience": 18,
        "Salary": 150000,
    },
    {
        "Employee_ID": 108,
        "Name": "Neha",
        "Department": "Sales",
        "Age": 29,
        "Experience": 5,
        "Salary": 75000,
    },
]

# --------------------------------------------------
# Create DataFrame
# --------------------------------------------------

df = pd.DataFrame(employees)

# --------------------------------------------------
# Save CSV
# --------------------------------------------------

df.to_csv(
    FILE_PATH,
    index=False
)

print("Employee dataset created successfully.")

print("\nFile:")
print(FILE_PATH.resolve())

print("\nDataset:")
print(df)

print("\nShape:")
print(df.shape)