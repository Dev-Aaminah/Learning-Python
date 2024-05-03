# Python has two kinds of functions: 1. user-defined and 2. built-in

# example of builtin function
big = max(1,2,3,4,5)
print(big)

largestChar = max("anbndbcdh")
print(largestChar)

# types of built-in func
# float()
# input()
# min()
# type()


# User defined function to add two number
def add():
    num1 = float(input('Enter first number: '))
    num2 = float(input('Enter second number: '))
    result=(num1+num2)
    print("Sum of", num1, "and" , num2, "is", result)
add()
