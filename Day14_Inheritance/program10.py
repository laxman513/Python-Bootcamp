# Program 10 - Child Constructor Without Parent Constructor

class Person:
    def __init__(self, name):
        self.name = name


class Student(Person):
    def __init__(self, age):
        self.age = age


student = Student(16)
print(student.age)

# student.name would fail because Person.__init__() was not called.
