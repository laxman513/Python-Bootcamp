import pandas as pd

data = {
    "Name": ["Rahul", "Priya", "Amit", "Sneha"],
    "Age": [25, 30, 35, 28],
    "Experience": [2, 5, 8, 4],
    "Salary": [50000, 70000, 90000, 65000]
}

df = pd.DataFrame(data)

df["Bonus"] = df["Salary"] * 0.10

print(df)