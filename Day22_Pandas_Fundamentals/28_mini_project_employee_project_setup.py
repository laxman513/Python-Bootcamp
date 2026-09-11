from pathlib import Path

import numpy as np
import pandas as pd


def main():
    # Create project data directory
    data_directory = Path("data")
    data_directory.mkdir(exist_ok=True)

    # Employee dataset
    data = {
        "Employee_ID": [101, 102, 103, 104, 105, 106, 107, 108],
        "Name": [
            "Rahul",
            "Priya",
            "Amit",
            "Sneha",
            "Kiran",
            "Anjali",
            "Vikram",
            "Neha"
        ],
        "Department": [
            "IT",
            "HR",
            "IT",
            "Finance",
            "IT",
            "HR",
            "Finance",
            "IT"
        ],
        "Age": [
            25,
            30,
            35,
            28,
            np.nan,
            32,
            40,
            27
        ],
        "Experience": [
            2,
            5,
            8,
            4,
            10,
            np.nan,
            15,
            3
        ],
        "Salary": [
            50000,
            65000,
            90000,
            70000,
            120000,
            75000,
            150000,
            np.nan
        ]
    }

    df = pd.DataFrame(data)

    # CSV output path
    file_path = data_directory / "employees.csv"

    # Save DataFrame
    df.to_csv(file_path, index=False)

    print("Employee dataset created successfully.")
    print()
    print(df)
    print()
    print("CSV file:", file_path.resolve())


if __name__ == "__main__":
    main()