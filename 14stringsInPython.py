# 'in' as logical operator

fruit = 'banana'
print('n' in fruit)
print('ana' in fruit)

if('a' in fruit):
    print('Yeah, Its there')

# Strings are objects, and objects have methods.
# one of the string object capability has is lower and upper.

greet = 'GREET'
print(greet.lower())

salam = 'assalam o alaikum'
print(salam.upper())

# type check
print(type(greet))
# below are print statement will let you know the things we can do with strings.
# print(dir(greet))

# search and replace
hello = 'Hello Aaminah'
change = hello.replace('Aaminah', 'Maam')
print(change)
# can replace a single char as well
change1 = hello.replace('o', 'x')
print(change1)

# strip whitespace
# it throws out the spaces. means removes.
gm = '    Good Morning    .'
print(gm.lstrip())
print(gm.rstrip())
print(gm.strip())

# prefixes, it checks whether a string starts with a something which we enter.
newString = 'Hey there.'
print(newString.startswith('Hello'))
# check if newString Starts with user's entered input
checkUser = input('Enter Something: ')
if newString.startswith(checkUser):
    print('Yes, it starts with "{}" :)'.format(checkUser))
else:
    print('Sorry, it does not start with "{}".'.format(checkUser))