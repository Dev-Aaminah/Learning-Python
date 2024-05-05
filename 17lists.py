# one way to do this
data = [1,2,3,4,5]
for each in data:
    print(each)

# the other way
print('the other way')
for i in [100,200,300,400,500]:
    print(i)


# strings are immutable whereas lists are mutable
data[3]= 350
print(data)

# item check in lists
print("length of item in data list is:",len(data))

# use of range in loops
friends = ['amela','sophia','linda']
for i in range(len(friends)):
    # print(i) # this will print index only
    friend = friends[i]
    print(i, "Hello", friend)

# concatination of strings is also possible
list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]
concat = list1+list2
print(concat)

# lists can be sliced
print(list1[2:5])
print(list2[:3])

# list methods
print(type(list2))
print(dir(list2))

# building list from scratch
stuff = list()
stuff.append('book')
stuff.append('all')
print(stuff)

# use of "in" and "not in" lists
cookies = [0,1,2,3,4,5]
print(9 in cookies)
print(20 not in cookies)

# sort strings
numbers = [3,0,2,3,1,4,5,8,6]
numbers.sort()
print(numbers)
# we can sort data on the basis of alphabets as well
friends.sort()
print(friends)

# funcs of lists
num = [22,33,44,55,66,77]
print(sum(num))
print(len(num))
print(max(num))
print(min(num))
print(sum(num)/len(num))

# split a list
quote = "A man is known by the company he keeps."
print(quote.split())
print(len(quote))
quoteStuff = quote.split()
print(len(quoteStuff))
print(quoteStuff[3])