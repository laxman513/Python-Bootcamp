import pandas as pd

data = {
    "Name": ["Rahul", "Priya", "Amit", "Sneha"],
    "Age": [25, 30, 35, 28],
    "Experience": [2, 5, 8, 4],
    "Salary": [50000, 70000, 90000, 65000]
}

df = pd.DataFrame(data)

high_salary = df[df["Salary"] > 70000]

print("Employees with salary greater than 70000:")
print(high_salary)

print("\nEmployees aged 30 or above:")
print(df[df["Age"] >= 30])