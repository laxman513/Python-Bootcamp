# Program 31 - Person and Student Practical Example

class Person:
    def __init__(self, name):
        self.name = name

    def display_name(self):
        print("Name:", self.name)


class Student(Person):
    def __init__(self, name, age):
        self.age = age
        super().__init__(name)

    def display_name(self):
        print("Name:", self.name)
        print("Age:", self.age)


student = Student("Laxman", 16)
student.display_name()
