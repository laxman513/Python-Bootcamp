# Program 15 - Changing Parent Order

class Father:
    def show(self):
        print("Father")


class Mother:
    def show(self):
        print("Mother")


class Child(Mother, Father):
    pass


child = Child()
child.show()
