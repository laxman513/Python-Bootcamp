def display_student(**kwargs):
    print(kwargs)
    print(type(kwargs))
    for key, value in kwargs.items():
        print(key, ":", value)


display_student(
    name="Rahul",
    age=20,
    city="Hyderabad"
)