# Program 18 - Polymorphic Transport
class Car:
    def move(self):
        print("Car is moving")

class Train:
    def move(self):
        print("Train is moving")

class Airplane:
    def move(self):
        print("Airplane is flying")

for transport in [Car(), Train(), Airplane()]:
    transport.move()
