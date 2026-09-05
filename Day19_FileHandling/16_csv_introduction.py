import csv

with open("students.csv", "r",  encoding="utf-8") as file:
    reader = csv.reader(file)

    for row in reader:
        # print(row)
        print(" | ".join(row))
