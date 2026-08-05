class Student:

    def __init__(self, name):
        self.name = name

    def greet(self, message):
        print(message, self.name)

student = Student("Laxman")

student.greet("Namasthe")