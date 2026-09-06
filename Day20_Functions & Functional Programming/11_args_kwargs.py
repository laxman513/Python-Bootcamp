def student_details(*args, **kwargs):
    print("Positional Arguments:")

    for value in args:
        print(value)

    print("Keyword Arguments:")

    for key, value in kwargs.items():
        print(key, ":", value)

student_details(
    10,
    20,
    30,
    name="Rahul",
    age=20,
    city="Hyderabad"
)