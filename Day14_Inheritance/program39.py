# Program 39 - Mini MRO Challenge

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


class E(B, C):
    def show(self):
        super().show()
        print("E")


class D(E):
    def show(self):
        super().show()
        print("D")


print("MRO:")
print(D.mro())

print("\nOutput:")
obj = D()
obj.show()

# MRO:
# D -> E -> B -> C -> A -> object
#
# Output:
# A
# C
# B
# E
# D
