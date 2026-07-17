student = {"name": "Laxman", "age": "45"}
student["city"] = "Hyderabad"
student["age"] = 46
print(student)
print(f"age:{student.get("age")}")
print(f"state:{student.get("state")}")
print(f"state:{student.get("state","Not Found")}")
print(f"state:{student.get("age", "asdfsdf")}")
print(f"state:{student["country"]}")

del student["age"]
print(student)
