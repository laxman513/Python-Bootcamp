students_python = {"Laxman", "Rahul", "Amit"}
students_java = {"Laxman", "Priya", "Amit"}

print("All unique students")
print(20*"-")
print(students_python | students_java)
print("-"*20)
print("Students enrolled in both courses")
print("-"*20)
print(students_python & students_java)
print(20*"-")
print("Students only in Python")
print(students_python - students_java)
print("Add Kiran to the Python set")
students_python.add("Kiran")
print("-"*20)
print("Remove Rahul from the Python set.")
students_python.remove("Rahul")
print("-"*20)
print("Final Pytho set")
print(students_python)

def greet():
    print("Hello")

print(greet())

def greet():
    print("Hello")
    return None
greet()

