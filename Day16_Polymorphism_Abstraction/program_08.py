# Program 08 - Overriding with Different Behavior
class Vehicle:
    def start(self):
        print("Vehicle starting")

class Car(Vehicle):
    def start(self):
        print("Car started")

class Bike(Vehicle):
    def start(self):
        print("Bike started")

for vehicle in [Car(), Bike()]:
    vehicle.start()
