import pandas as pd


data = {
    "Name": ["Rahul", "Priya", "Amit", "Sneha"],
    "Age": [25, 30, 35, 28],
    "Experience": [2, 5, 8, 4],
    "Salary": [50000, 70000, 90000, 65000]
}

df = pd.DataFrame(data)

print("\nFirst Row:")
print(df.loc[0])

print("\nRows 1 to 3:")
print(df.loc[1:3])