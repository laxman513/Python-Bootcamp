# Program 11 - Duck Typing
class Car:
    def start(self):
        print("Car started")

class Computer:
    def start(self):
        print("Computer started")

def start_machine(machine):
    machine.start()

start_machine(Car())
start_machine(Computer())
