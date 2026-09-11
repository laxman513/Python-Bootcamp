from pathlib import Path

import numpy as np
import pandas as pd


DATA_DIRECTORY = Path("data")
INPUT_FILE = DATA_DIRECTORY / "employees.csv"
OUTPUT_FILE = DATA_DIRECTORY / "employee_analysis_report.csv"


def load_data():
    """Load employee data from CSV."""

    return pd.read_csv(INPUT_FILE)


def clean_data(df):
    """Handle missing numeric values."""

    df = df.copy()

    numeric_columns = [
        "Age",
        "Experience",
        "Salary"
    ]

    for column in numeric_columns:
        df[column] = df[column].fillna(
            df[column].mean()
        )

    return df


def create_features(df):
    """Create useful employee categories."""

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


def display_basic_statistics(df):
    """Display basic employee statistics."""

    print("\n===== BASIC STATISTICS =====")

    print("Number of Employees:", len(df))
    print("Average Age:", round(df["Age"].mean(), 2))
    print("Average Experience:",
          round(df["Experience"].mean(), 2))

    print(
        "Average Salary:",
        round(df["Salary"].mean(), 2)
    )

    print(
        "Minimum Salary:",
        df["Salary"].min()
    )

    print(
        "Maximum Salary:",
        df["Salary"].max()
    )


def display_department_summary(df):
    """Display department-wise salary analysis."""

    print("\n===== DEPARTMENT SUMMARY =====")

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

    summary["Average_Salary"] = (
        summary["Average_Salary"].round(2)
    )

    print(summary)


def display_high_earners(df):
    """Display employees with salary >= 100000."""

    print("\n===== HIGH EARNERS =====")

    high_earners = (
        df.query("Salary >= 100000")
        .sort_values(
            by="Salary",
            ascending=False
        )
    )

    print(
        high_earners[
            [
                "Employee_ID",
                "Name",
                "Department",
                "Salary",
                "Salary_Category"
            ]
        ]
    )


def display_top_employees(df):
    """Display top three employees by salary."""

    print("\n===== TOP 3 EMPLOYEES =====")

    top_employees = (
        df.sort_values(
            by="Salary",
            ascending=False
        )
        .head(3)
    )

    print(
        top_employees[
            [
                "Employee_ID",
                "Name",
                "Department",
                "Salary",
                "Experience_Level"
            ]
        ]
    )


def display_experience_summary(df):
    """Display employee count by experience level."""

    print("\n===== EXPERIENCE LEVEL SUMMARY =====")

    summary = (
        df.groupby("Experience_Level")
        .agg(
            Employee_Count=("Employee_ID", "count"),
            Average_Salary=("Salary", "mean")
        )
        .reset_index()
    )

    summary["Average_Salary"] = (
        summary["Average_Salary"].round(2)
    )

    print(summary)


def save_report(df):
    """Save analyzed employee data to CSV."""

    df.to_csv(
        OUTPUT_FILE,
        index=False
    )

    print("\nReport saved successfully:")
    print(OUTPUT_FILE.resolve())


def main():

    print("======================================")
    print("       EMPLOYEE DATA ANALYZER")
    print("======================================")

    # Step 1: Load
    print("\nLoading employee data...")

    df = load_data()

    print("\nOriginal Dataset:")
    print(df)

    # Step 2: Inspect missing values
    print("\n===== MISSING VALUES =====")

    print(df.isna().sum())

    # Step 3: Clean
    print("\nCleaning missing values...")

    df = clean_data(df)

    # Verify no missing values
    print("\nMissing values after cleaning:")

    print(df.isna().sum())

    # Step 4: Feature engineering
    print("\nCreating employee categories...")

    df = create_features(df)

    # Step 5: Statistics
    display_basic_statistics(df)

    # Step 6: Department analysis
    display_department_summary(df)

    # Step 7: High earners
    display_high_earners(df)

    # Step 8: Experience analysis
    display_experience_summary(df)

    # Step 9: Top employees
    display_top_employees(df)

    # Step 10: Save final report
    save_report(df)

    print("\n======================================")
    print("       ANALYSIS COMPLETED")
    print("======================================")


if __name__ == "__main__":
    main()