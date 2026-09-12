from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt


FILE_PATH = Path("..") / "Day22_Pandas_Fundamentals" / "data" / "employees.csv"


df = pd.read_csv(FILE_PATH)

# Fill missing salary values
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())

# Calculate average salary by department
department_salary = (
    df.groupby("Department")["Salary"]
    .mean()
    .sort_values(ascending=False)
)


print("Average Salary by Department:")
print(department_salary)


plt.figure(figsize=(10, 6))

plt.bar(
    department_salary.index,
    department_salary.values
)

plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.title("Average Salary by Department")

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()