str = 'X-DSPAM-Confidence: 0.8475'

# find colon ':'
search = str.find(":")
# print(search)
piece = str[search+2:]
# print(piece)
val = float(piece)
print(val)
# print(val+42)
