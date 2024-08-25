# Create student class that takes name & marks of 3 subjects as arguments in constructor. Then create a method to print the average.

class Student:
    def __init__(self, name, marks1, marks2, marks3):
        self.name = name
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3
        
    def marks(self):
        sum = self.marks1 + self.marks2 + self.marks3
        avg = sum/3
        print(avg)
        
s1 = Student("Ali", 28, 32, 22)
s1.marks()