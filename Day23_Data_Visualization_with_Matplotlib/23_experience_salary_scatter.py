from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt

FILE_PATH = Path("..") / "Day22_Pandas_Fundamentals" / "data" / "employees.csv"

df = pd.read_csv(FILE_PATH)

# Keep only rows with valid Experience and Salary
clean_df = df.dropna(subset=["Experience", "Salary"])

print("Data used for visualization:")
print(clean_df[["Name", "Experience", "Salary"]])

plt.figure(figsize=(10, 6))

plt.scatter(
    clean_df["Experience"],
    clean_df["Salary"]
)

plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.title("Experience vs Salary")

plt.grid(True)

plt.tight_layout()

plt.show()