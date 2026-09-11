import pandas as pd


df = pd.DataFrame({
    "Name": ["Rahul", "Priya", "Amit", "Sneha"],
    "Age": [25, 30, 35, 28],
    "Salary": [50000, 70000, 90000, 65000]
})

print("Employee Data:")
print(df)

print("\nStatistics:")

print("Average Salary:", df["Salary"].mean())
print("Minimum Salary:", df["Salary"].min())
print("Maximum Salary:", df["Salary"].max())
print("Total Salary:", df["Salary"].sum())
print("Employee Count:", df["Salary"].count())