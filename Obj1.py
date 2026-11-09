class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


s1 = Student("Rishika", 20)
s2 = Student("Jahnavi", 18)
s3 = Student("Priya", 21)

s1.display()
s2.display()
s3.display()