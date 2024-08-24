class Student:  # class
    name = 'Aaminah'
    
s1 = Student()  # object
print(s1.name)

class Car:
    color = "Blue"
    brand = "Tesla"
    
car1 = Car()
print(car1.color)
print(car1.brand)


# Constructor || __init__ function
# all classes have a function called __init__(), which is always executed when the object is being initiated.

class Teacher:
    # default constructor
    def __init__(self):
        pass
    
    # parametrized constructor(constructor which has parameters other than 'self')
    def __init__(self, fullname, bps):
        # The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
        self.name = fullname
        # the data we save inside the class or object are called attributes.
        print(self)
        self.bps = bps
        print("Added a new row in database...")

new_teacher = Teacher(fullname="Aaminah", bps = 20)
print(new_teacher)
print(new_teacher.name)
new_teacher1 = Teacher(fullname="Seemab", bps = 17)
print(new_teacher1.name)
print(new_teacher.name, new_teacher1.name)
new_teacher2 = Teacher("Ujala", 19)
print(new_teacher2.name , new_teacher2.bps)