students = ["Ram", "Shyam", "Laxman", "David", "Krishna"]
print(f"first student: {students[0]}")
print(f"last student using negative indexing: {students[-1]}")
print(f"the total number of students: {len(students)}")
print("Changin Laxman to Rahul")
students[2] = "Rahul"
print(f"updated list: {students}")
print(f"second student: {students[1]}")
print(f"fourth student: {students[3]}")

marks = [85, 90, 78, 92, 88]

# Print the first mark
print(marks[0])
# Print the last mark
print(marks[-1])
# Change 78 to 80
marks[2] = 80
# Print the updated list
print(marks)
# Print the total number of marks
print(len(marks))
