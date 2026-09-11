import pandas as pd
import numpy as np


df = pd.DataFrame({
    "Name": ["Rahul", "Priya", "Amit", "Sneha", "Kiran"],
    "Age": [25, 30, 35, 28, 40],
    "Salary": [50000, 70000, 90000, 65000, 120000]
})

df["Salary_Category"] = np.where(
    df["Salary"] >= 70000,
    "High",
    "Normal"
)

print(df)