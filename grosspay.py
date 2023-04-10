#simple gross pay calculator

#hrs = input('Enter hours:')
#rate = input('Enter pay rate:')

#gross_pay = float(hrs) * float(rate)

#print('Pay:', gross_pay)



#modified gross pay calculator

#hrs = float(input('Enter hours:'))
#rate = float(input('Enter rate:'))

#if hrs <= 40:
#  gross_pay = hrs * rate
#else:
#  gross_pay = 40 * rate + ((hrs - 40) * (1.5 * rate))

#print(gross_pay)


# Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Pay should be the normal rate for hours up to 40 and time-and-a-half for the hourly rate for all hours worked above 40 hours. Put the logic to do the computation of pay in a function called computepay() and use the function to do the computation. The function should return a value. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). You should use input to read a string and float() to convert the string to a number. Do not worry about error checking the user input unless you want to - you can assume the user types numbers properly. Do not name your variable sum or use the sum() function.

def computepay(hrs, rate):
  if hrs > 40:
    return(40 * rate + ((hrs - 40) * (rate * 1.5)))
  else: 
    return(hrs * rate)

done = False

while done == False:
  try:
    hrs = float(input('Enter hours: '))
    rate = float(input('Enter rate: '))
    done = True
  except:
    print('Enter numbers only')
    done = False
  
print(computepay(hrs, rate))


