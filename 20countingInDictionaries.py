# This program aims to count the frequency of each word in a given line of text.

# Initialize an empty dictionary to store word counts.
counts = dict()

# Prompt the user to enter a line of text.
print('Enter a line of text: ')

# Read the input line.
line = input(' ')

# Split the line into individual words using whitespace as the delimiter and store them in a list.
words = line.split()

# Print the list of words extracted from the input line.
print('Words:', words)

# Inform the user that counting is in progress.
print('Counting')

# Iterate through each word in the list of words.
for word in words:
    # Check if the word is already present in the counts dictionary.
    # If it is present, retrieve its current count using the `get()` method,
    # otherwise, return 0 as the default value.
    counts[word] = counts.get(word, 0) + 1

# Print the final word counts stored in the counts dictionary.
print('Counts:', counts)



# Definite Loops and Dictionaries
items = {'Sana': 2, 'Warda': 3}
for item in items:
    print(item, items[item])

# list() method in dictionaries will print the keys in the dictionaries
jjj = {'Alpha':1, 'Beta':2, 'Gemma':3}
print(list(jjj))

# keys() method in dictionaries will print the keys in the dictionaries
print(jjj.keys())

# values() method in dictionaries will print the values in the dictionaries
print(jjj.values())

# items() method in dictionaries will print the items in the dictionaries
print(jjj.items())
print(list(jjj.items()))