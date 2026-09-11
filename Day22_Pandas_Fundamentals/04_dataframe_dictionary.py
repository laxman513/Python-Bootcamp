import pandas as pd

data = {
    "Name": ["Laxman", "Darahas"],
    "Age": [45, 17],
    "Experience": [10, 5],
    "Salary": [50000, 90000]
}

df = pd.DataFrame(data)

print(df)