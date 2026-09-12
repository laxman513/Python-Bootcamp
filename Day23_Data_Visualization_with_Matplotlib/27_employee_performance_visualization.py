from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


FILE_PATH = Path("..") / "Day22_Pandas_Fundamentals" / "data" / "employees.csv"

# --------------------------------------------------
# Load Data
# --------------------------------------------------

df = pd.read_csv(FILE_PATH)


# --------------------------------------------------
# Clean Data
# --------------------------------------------------

df["Experience"] = df["Experience"].fillna(
    df["Experience"].mean()
)

df["Salary"] = df["Salary"].fillna(
    df["Salary"].mean()
)

# --------------------------------------------------
# Create Experience Level
# --------------------------------------------------

df["Experience_Level"] = np.where(
    df["Experience"] >= 8,
    "Senior",
    np.where(
        df["Experience"] >= 5,
        "Mid",
        "Junior"
    )
)

# --------------------------------------------------
# Create Salary Category
# --------------------------------------------------
df["Salary_Category"] = np.where(
    df["Salary"] >= 100000,
    "High",
    "Standard"
)

print("===== Employee Categories =====")

print(
    df[
        [
            "Name",
            "Experience",
            "Salary",
            "Experience_Level",
            "Salary_Category"
        ]
    ]
)

# --------------------------------------------------
# Senior + High Salary Employees
# --------------------------------------------------

selected_employees = df[
    (df["Experience_Level"] == "Senior") 
    & (df["Salary_Category"] == "High")
]

print("\n===== Senior + High Salary Employees =====")

print(
    selected_employees[
        [
            "Name",
            "Department",
            "Experience",
            "Salary"
        ]
    ]
)


# --------------------------------------------------
# Visualization
# --------------------------------------------------

plt.figure(figsize=(10, 6))

standard = df[
    df["Salary_Category"] == "Standard"
]

plt.scatter(
    standard["Experience"],
    standard["Salary"],
    marker="o",
    label="Standard Salary"
)

# High salary employees
high = df[
    df["Salary_Category"] == "High"
]

plt.scatter(
    high["Experience"],
    high["Salary"],
    marker="x",
    label="High Salary"
)


plt.xlabel("Years of Experience")
plt.ylabel("Salary")

plt.title("Employee Experience vs Salary")

plt.legend()

plt.grid(True)

plt.tight_layout()

plt.show()