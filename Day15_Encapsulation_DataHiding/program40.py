# Final advanced property challenge
class Person:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip():
            self.__name = value
        else:
            print("Name cannot be empty")

class Student(Person):
    @property
    def name(self):
        return "Student: " + super().name

    @name.setter
    def name(self, value):
        if len(value) >= 3:
            Person.name.fset(self, value)
        else:
            print("Name must have at least 3 characters")

student = Student("Rahul")

student.name = "A"
print(student.name)

student.name = "Amit"
print(student.name)
