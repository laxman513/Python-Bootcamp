import requests

from student_utils.student import calculate_average, get_result


def main():
    student_name = "Rahul"
    marks = [85, 78, 92]

    average = calculate_average(marks)
    result = get_result(average)

    print("Student Name:", student_name)
    print("Marks:", marks)
    print("Average:", average)
    print("Result:", result)

    response = requests.get("https://www.example.com")

    print("Internet Status:", response.status_code)


if __name__ == "__main__":
    main()