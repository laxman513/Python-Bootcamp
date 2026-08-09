# Program 36 - isinstance() and issubclass() Together

class Person:
    pass


class Student(Person):
    pass


student = Student()

print("isinstance(student, Student):", isinstance(student, Student))
print("isinstance(student, Person):", isinstance(student, Person))
print("issubclass(Student, Person):", issubclass(Student, Person))
print("issubclass(Student, Student):", issubclass(Student, Student))
