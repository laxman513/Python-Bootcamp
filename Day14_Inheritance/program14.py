# Program 14 - Same Method in Two Parents

class Father:
    def show(self):
        print("Father")


class Mother:
    def show(self):
        print("Mother")


class Child(Father, Mother):
    pass


child = Child()
child.show()
