units=int(input('Enter the number of units: '))
total_amount=0
if units<=100:
    total_bill=units*2
elif units<=200:
    total_bill=(units-100)*3+100*2
else:
    total_bill=(units-200)*5+100*2+100*3
print('electricity bill',total_bill)
    
   