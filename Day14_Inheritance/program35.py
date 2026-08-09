# Program 35 - Multiple Inheritance with super() and MRO

class A:

    def show(self):
        print("A")


class B(A):

    def show(self):
        super().show()
        print("B")


class C(A):

    def show(self):
        super().show()
        print("C")


class D(B, C):

    def show(self):
        super().show()
        print("D")


obj = D()

print(D.mro())

obj.show()

# MRO:
# D -> B -> C -> A -> object
#
# Output from obj.show():
# A
# C
# B
# D
#
# Important:
# super() inside B does NOT directly mean A.
# It continues to the next class in D's MRO, which is C.
