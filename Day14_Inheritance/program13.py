# Program 13 - super() Does Not Have to Be the First Statement

class Person:
    def __init__(self, name):
        self.name = name


class Student(Person):
    def __init__(self, name, age):
        self.age = age
        super().__init__(name)


student = Student("Laxman", 16)

print(student.name)
print(student.age)
