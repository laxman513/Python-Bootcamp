import pandas as pd
import numpy as np


df = pd.DataFrame({
    "Name": ["Rahul", "Priya", "Amit", "Sneha"],
    "Age": [25, np.nan, 35, 28],
    "Salary": [50000, 70000, np.nan, 65000]
})


print("DataFrame:")
print(df)

print("\nMissing Value Matrix:")
print(df.isna())

print("\nMissing Values Per Column:")
print(df.isna().sum())