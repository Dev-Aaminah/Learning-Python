string = 'Banana'

# check length of string
# len is a func in py
print(len(string))

# check the letter in string at position/index [4]
print(string[4])

# loop to print all the letters in a string with index
fruit = 'pineapple'
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index = index + 1

# using for loop
print('For Loop')
fruit1 = 'strawberry'
# i = 0
# letter1 = fruit[i] 
for letter1 in fruit1:
    print(letter1)
    # i = i + 1


# check how many time a letter repeats in a string
sentence = 'Hello this is me, hope you are well :)'
count = 0
for alphabet in sentence:
    if alphabet == 'e':
        count = count + 1
print(count)


# simply the below loop will print all the letters in a string
for char in 'Aaminah':
    print(char)


# slicing strings
print('Slicing Strings')
sliceString = 'Hello Everyone'
print(sliceString[0:5])

print(sliceString[6:14])

# if you eliminate first or last indications, it will assume the very start or very end of the string. check the code below
print(sliceString[:]) # printing all the letters.
# and
print(sliceString[0:]) # again printing all the letters.
# and
print(sliceString[:14]) # and again printing all the letters.
# and
print(sliceString[:5])