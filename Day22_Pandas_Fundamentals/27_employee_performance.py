import pandas as pd
import numpy as np


df = pd.DataFrame({
    "Name": [
        "Rahul", "Priya", "Amit",
        "Sneha", "Kiran", "Vijay"
    ],
    "Department": [
        "IT", "HR", "IT",
        "HR", "IT", "Finance"
    ],
    "Age": [25, 30, 35, 28, 40, 32],
    "Experience": [2, 5, 8, 4, 12, 7],
    "Salary": [50000, 60000, 90000, 65000, 120000, 70000]
})

df["Experience Level"] = np.where(
    df["Experience"] >= 8,
    "Senior",
    "Junior"
)

df["Salary_Category"] = np.where(
    df["Salary"] >= 70000,
    "High",
    "Normal"
)


print("========== EMPLOYEE DATA ==========")
print(df)

print("\n========== EXPERIENCED EMPLOYEES ==========")
print(df[df["Experience"] >= 8])

print("\n========== SENIOR + HIGH SALARY ==========")

senior_high_salary = df[
    (df["Experience"] >= 8) & (df["Salary"] >= 70000)
]
print(senior_high_salary)

print("\n========== SALARY RANKING ==========")
salary_ranking = df.sort_values(
    "Salary",
    ascending=False
)
print(salary_ranking)