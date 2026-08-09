# Program 25 - isinstance()

class Person:
    pass


class Student(Person):
    pass


student = Student()

print(isinstance(student, Student))
print(isinstance(student, Person))
