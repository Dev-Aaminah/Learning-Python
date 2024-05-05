# file handle
fh = open('mbox.txt')
print(fh)

# to read file
for lx in fh:
    ly = lx.rstrip()
    print(ly.upper())