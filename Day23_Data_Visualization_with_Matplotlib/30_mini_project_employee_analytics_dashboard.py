from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# ==================================================
# 1. Configuration
# ==================================================

FILE_PATH = Path("data") / "employees.csv"


# ==================================================
# 2. Load Dataset
# ==================================================

df = pd.read_csv(FILE_PATH)


# ==================================================
# 3. Data Cleaning
# ==================================================

df["Age"] = df["Age"].fillna(
    df["Age"].mean()
)

df["Experience"] = df["Experience"].fillna(
    df["Experience"].mean()
)

df["Salary"] = df["Salary"].fillna(
    df["Salary"].mean()
)


# ==================================================
# 4. Salary Statistics
# ==================================================

average_salary = df["Salary"].mean()
minimum_salary = df["Salary"].min()
maximum_salary = df["Salary"].max()

average_experience = df["Experience"].mean()


# ==================================================
# 5. Department Analysis
# ==================================================

department_counts = (
    df["Department"]
    .value_counts()
)


department_salary = (
    df.groupby("Department")["Salary"]
    .mean()
    .sort_values(ascending=False)
)


# ==================================================
# 6. High Earners
# ==================================================

high_earners = df[
    df["Salary"] >= 100000
].sort_values(
    by="Salary",
    ascending=False
)


# ==================================================
# 7. Top Employees
# ==================================================

top_employees = df.sort_values(
    by="Salary",
    ascending=False
).head(5)


# ==================================================
# 8. Find Highest-Paid Employee
# ==================================================

highest_paid_index = np.argmax(
    df["Salary"].to_numpy()
)

highest_paid_employee = df.iloc[
    highest_paid_index
]


# ==================================================
# 9. Find Largest Department
# ==================================================

largest_department = (
    department_counts.idxmax()
)

largest_department_count = (
    department_counts.max()
)


# ==================================================
# 10. Print Analysis
# ==================================================

print("=" * 60)
print("           EMPLOYEE ANALYTICS REPORT")
print("=" * 60)


print("\n===== Salary Statistics =====")

print(
    f"Average Salary  : ₹{average_salary:,.2f}"
)

print(
    f"Minimum Salary  : ₹{minimum_salary:,.2f}"
)

print(
    f"Maximum Salary  : ₹{maximum_salary:,.2f}"
)


print("\n===== Experience Statistics =====")

print(
    f"Average Experience : "
    f"{average_experience:.2f} years"
)


print("\n===== Largest Department =====")

print(
    f"{largest_department} "
    f"({largest_department_count} employees)"
)


print("\n===== Highest Paid Employee =====")

print(
    f"Name       : {highest_paid_employee['Name']}"
)

print(
    f"Department : "
    f"{highest_paid_employee['Department']}"
)

print(
    f"Salary     : "
    f"₹{highest_paid_employee['Salary']:,.2f}"
)


print("\n===== High Earners =====")

print(
    high_earners[
        [
            "Name",
            "Department",
            "Experience",
            "Salary"
        ]
    ].to_string(index=False)
)


print("\n===== Top Employees =====")

print(
    top_employees[
        [
            "Name",
            "Department",
            "Salary"
        ]
    ].to_string(index=False)
)


# ==================================================
# 11. Create Dashboard
# ==================================================

plt.figure(figsize=(14, 10))


# --------------------------------------------------
# Chart 1 — Employee Count
# --------------------------------------------------

plt.subplot(2, 2, 1)

plt.bar(
    department_counts.index,
    department_counts.values
)

plt.title("Employee Count by Department")
plt.xlabel("Department")
plt.ylabel("Number of Employees")

plt.xticks(rotation=45)


# --------------------------------------------------
# Chart 2 — Average Salary
# --------------------------------------------------

plt.subplot(2, 2, 2)

plt.bar(
    department_salary.index,
    department_salary.values
)

plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")

plt.xticks(rotation=45)


# --------------------------------------------------
# Chart 3 — Experience vs Salary
# --------------------------------------------------

plt.subplot(2, 2, 3)

plt.scatter(
    df["Experience"],
    df["Salary"]
)

plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.title("Experience vs Salary")

plt.grid(True)


# --------------------------------------------------
# Chart 4 — Salary Distribution
# --------------------------------------------------

plt.subplot(2, 2, 4)

plt.hist(
    df["Salary"],
    bins=5
)

plt.xlabel("Salary")
plt.ylabel("Frequency")
plt.title("Salary Distribution")


# --------------------------------------------------
# Dashboard Layout
# --------------------------------------------------

plt.suptitle(
    "Employee Analytics Dashboard",
    fontsize=16
)

plt.tight_layout()

plt.show()