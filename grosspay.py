#simple gross pay calculator

#hrs = input('Enter hours:')
#rate = input('Enter pay rate:')

#gross_pay = float(hrs) * float(rate)

#print('Pay:', gross_pay)



#modified gross pay calculator
hrs = float(input('Enter hours:'))
rate = float(input('Enter rate:'))

if hrs <= 40:
  gross_pay = hrs * rate
else:
  gross_pay = 40 * rate + ((hrs - 40) * (1.5 * rate))

print(gross_pay)