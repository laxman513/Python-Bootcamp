# please run program 28 from Day22 first
 
from pathlib import Path

import matplotlib.pylab as plt

import pandas as pd

FILE_PATH = Path("..") / "Day22_Pandas_Fundamentals" / "data" / "employees.csv"

df = pd.read_csv(FILE_PATH)

# Fill missing salary values
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())

# Sort employee by Salary
df = df.sort_values(
    by="Salary",
    ascending=False
)

# Create bar chart
plt.figure(figsize=(10, 6))

plt.bar(df["Name"], df["Salary"])

plt.xlabel("Employee")
plt.ylabel("Salary")
plt.title("Employee Salary Comparison")

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()
