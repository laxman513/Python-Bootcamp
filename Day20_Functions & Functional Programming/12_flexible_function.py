def student_report(name, *marks, **details):

    print("Student Name:", name)
    print("Marks:", marks)

    if marks:
        average = sum(marks) / len(marks)
        print("Average:", average)

    for key, value in details.items():
        print(f"{key.capitalize()}:", value)

        
student_report(
    "Rahul",
    85,
    78,
    92,
    city="Hyderabad",
    course="Python"
)


def test(a, b, c, d, *args, x, y, z, **kwargs):
    print("a:", a)
    print("b:", b)
    print("c:", c)
    print("d:", d)

    print("args:", args)

    print("x:", x)
    print("y:", y)
    print("z:", z)

    print("kwargs:", kwargs)


test(
    10,
    20,
    30,
    40,
    50,
    60,
    70,
    x=100,
    y=200,
    z=300,
    city="Hyderabad",
    course="Python"
)   