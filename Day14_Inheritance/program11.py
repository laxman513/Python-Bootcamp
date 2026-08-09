# Program 11 - Calling Parent Constructor with super()

class Person:
    def __init__(self, name):
        self.name = name


class Student(Person):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age


student = Student("Laxman", 16)

print(student.name)
print(student.age)
