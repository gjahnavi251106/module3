from abc import ABC, abstractmethod

class Employee(ABC):

    @abstractmethod
    def display(self):
        pass


class EmployeeDetails(Employee):

    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display(self):
        print("Employee Name:", self.name)
        print("Employee Roll Number:", self.roll_no)
        print("Employee Marks:", self.marks)


s = EmployeeDetails("Janu", 10, 95)

s.display()