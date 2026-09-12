from pathlib import Path

import pandas as pd

# --------------------------------------------------
# File Path
# --------------------------------------------------

FILE_PATH = Path("data") / "employees.csv"


# --------------------------------------------------
# Load Data
# --------------------------------------------------

def load_data():
    return pd.read_csv(FILE_PATH)

# --------------------------------------------------
# Salary Statistics
# --------------------------------------------------

def salary_statistics(df):
    return {
        "average": df["Salary"].mean(),
        "minimum": df["Salary"].min(),
        "maximum": df["Salary"].max()
    }


# --------------------------------------------------
# Department Summary
# --------------------------------------------------
def department_summary(df):
    return (
        df.groupby("Department")
        .agg(
            Employee_Count=("Employee_ID", "count"),
            Average_Salary=("Salary", "mean"),
            Maximum_Salary=("Salary", "max"),
        )
        .sort_values(
            by="Average_Salary",
            ascending=False
        )
    )

# --------------------------------------------------
# High Earners
# --------------------------------------------------
def high_earners(df, salary_limit=100000):
    return df[
        df["Salary"] >= salary_limit
    ].sort_values(
        by="Salary",
        ascending=False
    )

# --------------------------------------------------
# Experience Summary
# --------------------------------------------------

def experience_summary(df):

    return {
        "average": df["Experience"].mean(),
        "minimum": df["Experience"].min(),
        "maximum": df["Experience"].max(),
    }

# --------------------------------------------------
# Top Employees
# --------------------------------------------------

def top_employees(df, count=5):

    return df.sort_values(
        by="Salary",
        ascending=False
    ).head(count)

# --------------------------------------------------
# Main
# --------------------------------------------------

def main():

    df = load_data()

    print("===== Employee Analytics =====")

    print("\nDataset:")
    print(df)

    # Salary statistics
    salary = salary_statistics(df)

    print("\n===== Salary Statistics =====")

    print(f"Average Salary : {salary['average']:.2f}")
    print(f"Minimum Salary : {salary['minimum']:.2f}")
    print(f"Maximum Salary : {salary['maximum']:.2f}")

    # Department summary
    print("\n===== Department Summary =====")

    print(
        department_summary(df)
    )

    # High earners
    print("\n===== High Earners =====")

    print(
        high_earners(df)
    )

    # Experience summary
    experience = experience_summary(df)

    print("\n===== Experience Statistics =====")

    print(
        f"Average Experience : "
        f"{experience['average']:.2f}"
    )

    print(
        f"Minimum Experience : "
        f"{experience['minimum']:.2f}"
    )

    print(
        f"Maximum Experience : "
        f"{experience['maximum']:.2f}"
    )

    # Top employees
    print("\n===== Top Employees =====")

    print(
        top_employees(df)
    )


if __name__ == "__main__":
    main()