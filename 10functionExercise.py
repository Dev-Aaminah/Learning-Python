hrs = input('Enter hours: ')
rph = input('Enter rate: ')

try:
        fhrs = float(hrs)
        frph = float(rph)
except:
        print('Enter a valid numeric input')
        quit()

def computepay(fhrs, frph):
    if fhrs>40:
        # print('Overtime \n')
        regPay = (fhrs) * (frph)
        otp = (fhrs - 40) * (frph * 0.5)
        otp = regPay + otp
        print('Pay', otp)
    else:
        # print('Regular \n')
        pay = (fhrs) * (frph)
        print('Pay ', pay)

    return
computepay(fhrs, frph)

def thing():
    print('Hello')
 
print('There')