"""
=========================================================
Python Bootcamp - Day 7
Topic: Dictionaries
Prepared for: Laxman
=========================================================
"""

print("="*60)
print("PROGRAM 1 - Create Dictionary")
student = {"name":"Laxman","age":46,"city":"Hyderabad"}
print(student)

print("\nPROGRAM 2 - Access Values")
print(student["name"])
print(student.get("age"))
print(student.get("salary"))
print(student.get("salary","Not Available"))

print("\nPROGRAM 3 - Add New Key")
student["salary"]=50000
print(student)

print("\nPROGRAM 4 - Update Existing Key")
student["city"]="Bengaluru"
print(student)

print("\nPROGRAM 5 - pop()")
removed = student.pop("salary")
print("Removed:", removed)
print(student)

print("\nPROGRAM 6 - del")
del student["city"]
print(student)

print("\nPROGRAM 7 - clear()")
temp = student.copy()
temp.clear()
print(temp)

print("\nPROGRAM 8 - keys()")
print(student.keys())

print("\nPROGRAM 9 - values()")
print(student.values())

print("\nPROGRAM 10 - items()")
print(student.items())

print("\nPROGRAM 11 - Loop through Keys")
for key in student:
    print(key)

print("\nPROGRAM 12 - Loop through Values")
for value in student.values():
    print(value)

print("\nPROGRAM 13 - Loop through Items")
for key, value in student.items():
    print(f"{key} = {value}")

print("\nPROGRAM 14 - Print Tuple Returned by items()")
for item in student.items():
    print(item)

print("\nPROGRAM 15 - Access Value Using Key in Loop")
for key in student:
    print(key, student[key])

print("\nPROGRAM 16 - update() Add New Key")
student.update({"department":"AI"})
print(student)

print("\nPROGRAM 17 - update() Update Existing Key")
student.update({"age":47})
print(student)

print("\nPROGRAM 18 - update() Multiple Keys")
student.update({"experience":15,"country":"India"})
print(student)

print("\nPROGRAM 19 - Assignment vs Copy")
student1={"name":"Laxman"}
student2=student1
student2["age"]=46
print("student1:",student1)
print("student2:",student2)

print("\nPROGRAM 20 - copy()")
student1={"name":"Laxman"}
student2=student1.copy()
student2["age"]=46
print("student1:",student1)
print("student2:",student2)

print("\nPROGRAM 21 - Employee Mini Project")
employee={
    "id":101,
    "name":"Laxman",
    "department":"IT"
}
employee.update({"salary":50000})
employee.update({"department":"AI"})

print("\nEmployee Dictionary")
print(employee)

print("\nKeys")
print(employee.keys())

print("\nValues")
print(employee.values())

print("\nItems")
print(employee.items())

print("\nTotal Fields")
print(len(employee))

print("\nFormatted Output")
for key,value in employee.items():
    print(f"{key} : {value}")

print("\nEnd of Day 7 Programs")
