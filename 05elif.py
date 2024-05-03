x = 'A'

if x=='D':
    print('Its D')
elif x=='A':
    print('Its A')
else :
    print('Nothing')
print('All Done!')


user = input('Enter your Age: ')
userVal = int(user)
print('You are', userVal, 'years old.')
if(userVal>18):
    print("Your age is more than 18")
elif userVal<18:
    print('You are under 18')
elif userVal < 100:
    print("Your age is less than 100")
elif userVal>18 and userVal < 100:
    print("Your age is more than 18 and less than 100")
else:
    print('All Done!')