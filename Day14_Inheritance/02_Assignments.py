# ==========================================================
# Day 14 - Assignments
# Topic: Inheritance, super(), Multiple Inheritance & MRO
# ==========================================================


# ==========================================================
# Assignment 1 - Single Inheritance
# ==========================================================

class Person:

    def __init__(self, name):
        self.name = name

    def display_name(self):
        print("Name:", self.name)


class Student(Person):

    def display_age(self, age):
        print("Age:", age)


student = Student("Laxman")

student.display_name()
student.display_age(16)


# ==========================================================
# Assignment 2 - Inheritance with super()
# ==========================================================

class Employee:

    def __init__(self, name):
        self.name = name


class Developer(Employee):

    def __init__(self, name, language):
        super().__init__(name)
        self.language = language

    def display(self):
        print("Name:", self.name)
        print("Language:", self.language)


developer = Developer("Laxman", "Python")

developer.display()


# ==========================================================
# Assignment 3 - Multilevel Inheritance
# ==========================================================

class Person:

    def person_info(self):
        print("I am a person")


class Employee(Person):

    def employee_info(self):
        print("I am an employee")


class Manager(Employee):

    def manager_info(self):
        print("I am a manager")


manager = Manager()

manager.person_info()
manager.employee_info()
manager.manager_info()


# ==========================================================
# Assignment 4 - Multiple Inheritance
# ==========================================================

class Father:

    def father_info(self):
        print("Father information")


class Mother:

    def mother_info(self):
        print("Mother information")


class Child(Father, Mother):

    def child_info(self):
        print("Child information")


child = Child()

child.father_info()
child.mother_info()
child.child_info()


# ==========================================================
# Assignment 5 - Method Resolution Order
# ==========================================================

class A:

    def show(self):
        print("A")


class B(A):

    def show(self):
        print("B")


class C(A):

    def show(self):
        print("C")


class D(B, C):
    pass


obj = D()

print("\nMRO:")
print(D.mro())

print("\nMethod output:")
obj.show()


# ==========================================================
# Assignment 6 - Diamond Inheritance
# ==========================================================

class Animal:

    def eat(self):
        print("Eating")


class Dog(Animal):

    def sound(self):
        print("Barking")


class Cat(Animal):

    def sound(self):
        print("Meowing")


class Puppy(Dog, Cat):
    pass


puppy = Puppy()

puppy.eat()
puppy.sound()


# ==========================================================
# Assignment 7 - isinstance()
# ==========================================================

class Vehicle:
    pass


class Car(Vehicle):
    pass


car = Car()

print("\nIs Car instance of Car?")
print(isinstance(car, Car))

print("Is Car instance of Vehicle?")
print(isinstance(car, Vehicle))


# ==========================================================
# Assignment 8 - issubclass()
# ==========================================================

print("\nIs Car subclass of Vehicle?")
print(issubclass(Car, Vehicle))

print("Is Car subclass of Car?")
print(issubclass(Car, Car))


# ==========================================================
# Assignment 9 - Explicit Parent Method Calls
# ==========================================================

class Father:

    def show(self):
        print("Father")


class Mother:

    def show(self):
        print("Mother")


class Child(Father, Mother):

    def show_all(self):
        Father.show(self)
        Mother.show(self)


child = Child()

child.show_all()


# ==========================================================
# Assignment 10 - super() with Multiple Inheritance
# ==========================================================

class Base:

    def show(self):
        pass


class Father(Base):

    def show(self):
        print("Father")
        super().show()


class Mother(Base):

    def show(self):
        print("Mother")
        super().show()


class Child(Father, Mother):

    def show(self):
        print("Child")
        super().show()


child = Child()

print("\nMRO:")
print(Child.mro())

print("\nOutput:")
child.show()