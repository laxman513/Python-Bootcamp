from pathlib import Path

import numpy as np
import pandas as pd


FILE_PATH = Path("data") / "employees.csv"

def load_employee_data():
    """Load employee data from CSV."""
    df = pd.read_csv(FILE_PATH)

    return df

def clean_employee_data(df):
    """Fill missing numeric values using means."""
    df = df.copy()

    numeric_columns = ["Age", "Experience", "Salary"]

    for column in numeric_columns:
        df[column] = df[column].fillna(df[column].mean())

    return df

def add_employee_categories(df):
    """Add experience and salary categories."""

    df = df.copy()

    df["Experience_Level"] = np.where(
         df["Experience"] >= 8,
         "Senior",
         np.where(
             df["Experience"] >= 4,
            "Mid-Level",
            "Junior"
        )
    )

    df["Salary_Category"] = np.where(
        df["Salary"] >= 100000,
        "High",
        np.where(
            df["Salary"] >= 70000,
            "Medium",
            "Low"
        )
    )

    return df

def get_department_summary(df):
    """Return department-wise salary summary."""

    summary = (
        df.groupby("Department")
        .agg(
            Employee_Count=("Employee_ID", "count"),
            Average_Salary=("Salary", "mean"),
            Minimum_Salary=("Salary", "min"),
            Maximum_Salary=("Salary", "max")
        )
        .reset_index()
    )

    return summary

def get_high_earners(df):
    """Return employees earning at least 100000."""

    high_earners = df[df["Salary"] >= 100000]

    return high_earners.sort_values(
        by="Salary",
        ascending=False
    )

def get_top_employees(df, count=3):
    """Return top employees based on salary."""

    return df.sort_values(
        by="Salary",
        ascending=False
    ).head(count)

def main():
    print("Loading employee data...")
    print()

    df = load_employee_data()

    print("Original Data:")
    print(df)

    print()
    print("Cleaning data...")

    df = clean_employee_data(df)

    print()
    print("Adding employee categories...")

    df = add_employee_categories(df)

    print()
    print("Department Summary:")
    print(get_department_summary(df))

    print()
    print("High Earners:")
    print(get_high_earners(df))

    print()
    print("Top 3 Employees:")
    print(get_top_employees(df))


if __name__ == "__main__":
    main()

    