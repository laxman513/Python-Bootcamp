student = ("Laxman", 46, "Hyderabad", "Java Developer")
print(f"Student:{student}")

name, age, city, profession = student
print(f"Name:{name}")
print(f"Age:{age}")
print(f"City:{city}")
print(f"Profession:{profession}")

print(f"Total number elements:{len(student)}")
print(f"TYpe of student:{type(student)}")


def get_user():
    return "laxman", 46
name, age = get_user
print(name)

