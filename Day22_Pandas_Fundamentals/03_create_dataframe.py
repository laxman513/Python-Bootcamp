import pandas as pd

data = [
    ["Laxman", 45, 10, 50000],
    ["Darahas", 17, 5, 55000],
    ["Dhanush", 15, 7, 90000],
    ["Saritha", 40, 9, 40000]
]

columns = ["Name", "Age", "Experience", "Salary"]

df = pd.DataFrame(data, columns=columns)

print(df)