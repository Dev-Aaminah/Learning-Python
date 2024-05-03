# The try and except blocks in Python are used for exception handling.

astr = 'Hello James'
try:
    istr = int(astr)
except:
    istr = -1
print('First', istr)