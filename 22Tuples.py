# Tuples are immutable, lists are mutable

tuples = ('H', 'I', 'J')
print(tuples)
print(tuples[2])

y = (1,2,3,4,5)
for each in y:
    print(each)
print("Largest value in this tuple is:", max(y))

# tuples and assignment
(x,y) = (1,'Aaminah')
print(x,y)
print(y)

# sort list of tuples
d = {'A':1, 'B':2, 'E':5, 'C':3, 'D':4}
print(d.items())
print(sorted(d.items()))
# print key value pairs with for loop
for k, v in sorted(d.items()):
    print(k,v)