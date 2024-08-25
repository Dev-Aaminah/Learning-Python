class Study:
    name = 'Computer Science'
    
    def __init__(self, degree, year):
        self.degree = degree
        self.year = year
        
    @staticmethod   # decorator
    def subject():  # no (self) parameter here. 
        print("Aaminah has passed the degree in", dbms.year)
        
dbms = Study("BSSE", 2024)
print(dbms.name, dbms.degree, dbms.year)
dbms.subject()