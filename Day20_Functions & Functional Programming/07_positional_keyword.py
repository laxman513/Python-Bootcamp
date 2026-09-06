def display_student(name, age, city):
    print("Name:", name)
    print("Age:", age)
    print("City:", city)


print("Positional:")
display_student("Rahul", 20, "Hyderabad")


print("\nKeyword:")
display_student(
    name="Rahul",
    age=20,
    city="Hyderabad"
)