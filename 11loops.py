# indefinte loop (while loop)

n=5
while n>0:
    print(n)
    n=n-1

# definite loop (for loop)

for i in [1,2,3,4,5]:
    print(i)

# find largest number
largest = 0
print('Initial largest value', largest)
for num in [45,5,2,10,9,75,68]:
    if num>largest:
        largest = num
print('Final largest value', largest)


# find smallest number
smallest = 100
print('Initial value', smallest)
for num in [45,5,2,10,9,75,68]:
    if num<smallest:
        smallest = num
print('Final smallest value', smallest)

