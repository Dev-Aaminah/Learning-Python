hrs = input('Enter Hours: ')
rate = input('Enter Rate: ')
try:
        fhrs = float(hrs)
        frate = float(rate)
except:
        print('Enter a valid numeric input')
        quit()
if fhrs>40:
        # print('Overtime \n')
        regPay = (fhrs) * (frate)
        otp = (fhrs - 40) * (frate * 0.5)
        otp = regPay + otp
        print(otp)
else:
        # print('Regular \n')
        pay = (fhrs) * (frate)
        print('Pay: ', pay)