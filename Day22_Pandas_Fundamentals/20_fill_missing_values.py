import pandas as pd
import numpy as np


df = pd.DataFrame({
    "Name": ["Rahul", "Priya", "Amit", "Sneha"],
    "Age": [25, np.nan, 35, 28],
    "Salary": [50000, 70000, np.nan, 65000]
})

print("Before Filling Missing Values:")
print(df)

age_mean = df["Age"].mean()
salary_mean = df["Salary"].mean()

print("Age Mean:", age_mean)
print("Salary Mean:", salary_mean)

df["Age"] = df["Age"].fillna(age_mean)
df["Salary"] = df["Salary"].fillna(salary_mean)

print("After Filling Missing Values:")
print(df)