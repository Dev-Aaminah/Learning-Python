# Remember python always takes input as text , not number
# So if we want to deal with numeric data, we'll be needing to first convert it.

inputUser = input('Europe Floor?')
convertStringToNumber = int(inputUser)+1
print('US Floor', convertStringToNumber)