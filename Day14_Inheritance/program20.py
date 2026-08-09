# Program 20 - Reverse Parent Order

class A:
    def show(self):
        print("A")


class B:
    def show(self):
        print("B")


class C(B, A):
    pass


print(C.mro())

obj = C()
obj.show()
