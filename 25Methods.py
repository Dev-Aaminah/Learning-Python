# Class can store two things. i.e. 1- Data(attributes) 2- Methods
# Methods are functions that belong to object.

# Class
class Animal():
    # constructor
    def __init__(self, color, name):
        self.color = color
        self.name = name
        
    # methods
    def bark(self):
        print(self.color, self.name, "barks")
# Object
dog = Animal("Brown","Dog")
dog.bark()