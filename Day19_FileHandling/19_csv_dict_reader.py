import csv

with open("students.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(
            f"Name: {row['Name']}, "
            f"Age: {row['Age']}, "
            f"Marks: {row['Marks']}"
        )