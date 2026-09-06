# Student result processing functions

def calculate_average(*marks):
    if not marks:
        return 0

    return sum(marks) / len(marks)


def get_result(average):
    if average >= 40:
        return "PASS"

    return "FAIL"


def get_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    elif average >= 40:
        return "E"
    else:
        return "F"


def process_marks(marks):
    # Add 5 bonus marks to every subject
    updated_marks = list(map(lambda mark: mark + 5, marks))

    # Keep only passing marks
    passing_marks = list(filter(lambda mark: mark >= 40, updated_marks))

    return updated_marks, passing_marks