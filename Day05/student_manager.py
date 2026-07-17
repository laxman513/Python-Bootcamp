students = ["Ram", "Shyam", "David"]
print("Original List:", students)

students.append("Krishna")
students.insert(1, "Rahul")
students.remove("Shyam")

removed_student = students.pop()
print("Removed Student:", removed_student)

students.sort()
print("Students after sort():", students)

students.reverse()
print("Students after reverse():", students)

print("Final List:", students)
print("Total No.of Students:", len(students))
print("First student:", students[0])
print("Last Student:", students[-1])
print("-------------------------")
stud = ["Ram", "Shyam", "David"]
stud.sort(reverse=True)
print(stud)
stud.reverse()
print(stud)

print("===================")
names = ["Ram", "Shyam"]

print(names.append)

print(names.append("David"))

print(names)

print("@@@@@@@@@@@@@@@@@@@@@@")
def hello():
    print("Hello")

x = hello

print("Step 1")

x

print("Step 2")

x()

print("Step 3")