from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt

FILE_PATH = Path("..") / "Day22_Pandas_Fundamentals" / "data" / "employees.csv"

# --------------------------------------------------
# 1. Load Data
# --------------------------------------------------
df = pd.read_csv(FILE_PATH)

# --------------------------------------------------
# 2. Clean Data
# --------------------------------------------------
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())

clean_experience_df = df.dropna(subset=["Experience", "Salary"])

# --------------------------------------------------
# 3. Prepare Analysis Data
# --------------------------------------------------
department_counts = df["Department"].value_counts()

department_salary = (
    df.groupby("Department")["Salary"]
    .mean()
    .sort_values(ascending=False)
)

experience = clean_experience_df["Experience"]
salary = clean_experience_df["Salary"]

# --------------------------------------------------
# 4. Create Dashboard
# --------------------------------------------------

plt.figure(figsize=(14, 10))

# ----------------------------------------
# Chart 1 — Employee Count
# ----------------------------------------
plt.subplot(2, 2, 1)
plt.bar(
    department_counts.index,
    department_counts.values
)
plt.title("Employees by Department")
plt.xlabel("Department")
plt.ylabel("Employees")

plt.xticks(rotation=45)

# ----------------------------------------
# Chart 2 — Average Salary
# ----------------------------------------
plt.subplot(2, 2, 2)

plt.bar(
    department_salary.index,
    department_salary.values
)

plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")

plt.xticks(rotation=45)

# ----------------------------------------
# Chart 3 — Experience vs Salary
# ----------------------------------------
plt.subplot(2, 2, 3)

plt.scatter(
    experience,
    salary
)

plt.title("Experience vs Salary")
plt.xlabel("Experience")
plt.ylabel("Salary")

plt.grid(True)

# ----------------------------------------
# Chart 4 — Salary Distribution
# ----------------------------------------

plt.subplot(2, 2, 4)

plt.hist(
    salary,
    bins=5
)

plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Frequency")

# ----------------------------------------
# Display Dashboard
# ----------------------------------------

plt.tight_layout()

plt.show()