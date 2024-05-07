# dictionaries are collection of key , value pair.
cabinet = dict()
cabinet['summer'] = 12
cabinet['winter'] = 3
cabinet['spring'] = 17
cabinet['autumn'] = 89
print(cabinet)
print(cabinet['summer'])
# we can update value of any key
cabinet['spring'] = cabinet['spring']+3
print(cabinet)

# we are making a dictionary which will look for the names and when we encounter a new name, we need to add a new entry in the dictionary. and if this is the second or later time we have seen the name, we simply add one to the count.
counts = dict()
vehicle = ['scooty', 'bicyle', 'car', 'bus', 'rickshaw', 'aeroplane', 'car', 'bus', 'rickshaw']
for each in vehicle:
    if each not in counts:
        counts[each]=1
    else:
        counts[each] = counts[each]+1
print(counts)


# the other way to do the same thing
stuff = dict()
names = ['Sidra', 'Sadia', 'Sana', 'Safa', 'Samra', 'Safa']
for name in names:
    stuff[name] = stuff.get(name, 0) + 1
print(stuff) 