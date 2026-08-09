# Program 09 - Constructor Inheritance

class Person:
    def __init__(self, name):
        self.name = name


class Student(Person):
    pass


student = Student("Laxman")
print(student.name)
