# Program 28 - Explicit Parent Method Calls

class Father:
    def show(self):
        print("Father")


class Mother:
    def show(self):
        print("Mother")


class Child(Father, Mother):
    def show(self):
        Father.show(self)
        Mother.show(self)
        print("Child")


child = Child()
child.show()
