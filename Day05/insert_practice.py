students = ["Ram", "Shyam", "David"]

print("fOriginal List:{studetns}")

students.insert(1, "Rahul")
print("After insert Rahul:", students)

students.insert(0, "Krishna")
print("After insert Krishna:", students)

students.insert(100, "Laxman")
print(f"After insert Laxman:{students}")

students.insert(-1, "Lucky")
print(f"After insert Lucky:{students}")

students.insert(-2, "Chikku")
print(f"After insert Chikku:{students}")

students.append(2)
students.remove(2)

