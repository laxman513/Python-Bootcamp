# Program 24 - MRO and super() Trace

class A:
    def show(self):
        print("A")


class B(A):
    def show(self):
        print("Entering B")
        super().show()
        print("Leaving B")


class C(A):
    def show(self):
        print("Entering C")
        super().show()
        print("Leaving C")


class D(B, C):
    def show(self):
        print("Entering D")
        super().show()
        print("Leaving D")


print(D.mro())

obj = D()
obj.show()
