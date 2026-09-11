import pandas as pd


df = pd.DataFrame({
    "Name": ["Rahul", "Priya", "Amit", "Sneha", "Kiran"],
    "Age": [25, 30, 35, 28, 40],
    "Experience": [2, 5, 8, 4, 12],
    "Salary": [50000, 70000, 90000, 65000, 120000]
})

print("Employees with salary > 70000:")
print(df.query("Salary > 70000"))
print(df[df["Salary"] > 70000])

print("\nEmployees with Age >= 30:")
print(df.query("Age >= 30"))

print("\nEmployees with Experience >= 5 and Salary > 70000:")
print(df.query("Experience >= 5 and Salary > 70000"))