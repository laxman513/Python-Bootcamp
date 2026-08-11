# Program 38 - Bank Payment System Base Class
from abc import ABC, abstractmethod

class Payment(ABC):
    def __init__(self, amount):
        self.__amount = amount

    @property
    def amount(self):
        return self.__amount

    @abstractmethod
    def process(self):
        pass
