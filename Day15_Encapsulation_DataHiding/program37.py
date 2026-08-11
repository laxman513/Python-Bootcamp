# Overriding a getter without defining a setter
class Person:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

class Student(Person):
    @property
    def name(self):
        return "Student: " + super().name

student = Student("Rahul")
print(student.name)
# student.name = "Amit"  # AttributeError: child property has no setter
