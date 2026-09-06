from student_result_functions_29 import (
    calculate_average,
    get_result,
    get_grade,
    process_marks
)


def display_student_result(student):
    name = student["name"]
    marks = student["marks"]

    updated_marks, passing_marks = process_marks(marks)

    average = calculate_average(*updated_marks)

    result = get_result(average)

    grade = get_grade(average)

    print("Student:", name)
    print("Original Marks:", marks)
    print("Updated Marks:", updated_marks)
    print("Passing Marks:", passing_marks)
    print("Average:", average)
    print("Result:", result)
    print("Grade:", grade)
    print("-" * 40)


def main():

    students = [
        {
            "name": "Rahul",
            "marks": [85, 78, 92]
        },
        {
            "name": "Priya",
            "marks": [65, 72, 81]
        },
        {
            "name": "Arjun",
            "marks": [35, 42, 38]
        }
    ]

    for student in students:
        display_student_result(student)


if __name__ == "__main__":
    main()