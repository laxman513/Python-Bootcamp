from pathlib import Path
import json

data_directory = Path("student_data")
data_directory.mkdir(exist_ok=True)

student_file = data_directory / "students,json"

if not student_file.exists():
    with open(student_file, "w", encoding="utf-8") as file:
        json.dump([], file, indent=4)

    print("Student Data created Successfully!!!")
else:
    print("Student Data file already exist!!")

print("File:", student_file)
print("File exists:", student_file.exists())