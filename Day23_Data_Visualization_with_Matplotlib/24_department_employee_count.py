from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt


FILE_PATH = Path("..") / "Day22_Pandas_Fundamentals" / "data" / "employees.csv"


df = pd.read_csv(FILE_PATH)


department_counts = df["Department"].value_counts()


print("Employee Count by Department:")
print(department_counts)

plt.figure(figsize=(10, 6))

plt.bar(
    department_counts.index,
    department_counts.values
)

plt.xlabel("Department")
plt.ylabel("Number of Employees")
plt.title("Employee Count by Department")

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()