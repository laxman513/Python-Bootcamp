# Program 16 - Display MRO

class Father:
    pass


class Mother:
    pass


class Child(Father, Mother):
    pass


print(Child.mro())
