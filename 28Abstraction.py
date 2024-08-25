# Abstraction
# Hiding the implementation details of a class and only shpwing the essential features to the user.
# E.g. Driver has no idea about working of engine.

class Car:
    def __init__(self):
        self.name = False
        self.brand = False
        self.cc = False
    
    @staticmethod
    def start():
        name = "Car"
        brand = "Tesla"
        print("Branded Car Started ...")
            
car1 = Car()
car1.start()