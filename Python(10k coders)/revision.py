num=int(input('enter the number:'))
if num<9 and num>0:
    print('single digit')
elif num>9 and num<=99:
    print('two digit')
elif num>100 and num<=999:
    print('third digit')
else:
    print('more than 3 digit')
    