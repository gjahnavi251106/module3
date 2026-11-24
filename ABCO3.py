from abc import ABC, abstractmethod

class Calculator(ABC):

    @abstractmethod
    def display(self):
        pass


class CalculatorDetails(Calculator):

    def __init__(self, add, sub, muil, div):
        self.add = add
        self.sub = sub
        self.muil = muil
        self.div = div

    def display(self):
        print("Addition:", self.add)
        print("Subtraction:", self.sub)
        print("Multiplication:", self.muil)
        print("Division:", self.div)


s = CalculatorDetails(10, 5, 20, 4)

s.display()