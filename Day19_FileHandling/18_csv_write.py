import csv

students = [
    ["Laxman", 20, 85],
    ["Darahas", 21, 92],
    ["Dhanush", 19, 72]
]

with open("students_output.csv", "w", newline="", encoding="utf-8") as file:

    writer = csv.writer(file)

    writer.writerow(["Name", "Age", "Marks"])

    writer.writerows(students)

print("CSV file created successfully.")