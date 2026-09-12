# please run program 28 from Day22 first

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


FILE_PATH = Path("..") / "Day22_Pandas_Fundamentals" / "data" / "employees.csv"


def main():

    # Load employee data
    df = pd.read_csv(FILE_PATH)

    # Handle missing salary values
    df["Salary"] = df["Salary"].fillna(
        df["Salary"].mean()
    )

    # Sort employees by salary
    salary_data = df.sort_values(
        by="Salary",
        ascending=False
    )

    plt.figure(figsize=(10, 6))

    plt.bar(
        salary_data["Name"],
        salary_data["Salary"]
    )

    plt.xlabel("Employee")
    plt.ylabel("Salary")
    plt.title("Employee Salary Comparison")

    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.show()


if __name__ == "__main__":
    main()