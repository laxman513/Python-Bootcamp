from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt


FILE_PATH = Path("..") / "Day22_Pandas_Fundamentals" / "data" / "employees.csv"

# --------------------------------------------------
# Load Data
# --------------------------------------------------

df = pd.read_csv(FILE_PATH)


# --------------------------------------------------
# Handle Missing Salary
# --------------------------------------------------

df["Salary"] = df["Salary"].fillna(df["Salary"].mean())


# --------------------------------------------------
# Salary Statistics
# --------------------------------------------------

average_salary = df["Salary"].mean()
minimum_salary = df["Salary"].min()
maximum_salary = df["Salary"].max()


print("===== Salary Analysis =====")

print(f"Average Salary : {average_salary:.2f}")
print(f"Minimum Salary : {minimum_salary:.2f}")
print(f"Maximum Salary : {maximum_salary:.2f}")

# --------------------------------------------------
# High Earners
# --------------------------------------------------

high_earners = df[df["Salary"] >= 100000]


print("\n===== High Earners =====")

print(
    high_earners[
        ["Name", "Department", "Salary"]
    ]
)

# --------------------------------------------------
# Sort Employees
# --------------------------------------------------

salary_data = df.sort_values(
    by="Salary",
    ascending=False
)


print("\n===== Salary Ranking =====")

print(
    salary_data[
        ["Name", "Salary"]
    ]
)


# --------------------------------------------------
# Visualization
# --------------------------------------------------

plt.figure(figsize=(11, 6))

plt.bar(
    salary_data["Name"],
    salary_data["Salary"]
)

plt.xlabel("Employee")
plt.ylabel("Salary")
plt.title("Employee Salary Ranking")

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()