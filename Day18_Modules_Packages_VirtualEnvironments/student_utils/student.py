def calculate_average(marks):
    """Calculate the average of the marks."""
    return sum(marks) / len(marks)


def get_result(average):
    """Return PASS if average is 40 or above, otherwise FAIL."""
    if average >= 40:
        return "PASS"

    return "FAIL"