import csv

with open("students.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)

    header = next(reader)

    print("Header")

    print(" | ".join(header))

    print("\nStudent Data")

    for row in reader:
        print(" | ".join(row))
        
