#  Program to explain input output

#cash = input('Enter your cash:') --> single input
pin, cash = input('Enter your pin and cash:').split(',')
print('Pin and cash are:', pin, cash)
print('Type of cash is:', type(cash))
typeValue = int(cash)


atmAmount = 50000
remainingAmount = atmAmount - typeValue
print('Type of value is:', type(typeValue), 'Take your cash:', cash, remainingAmount, sep='@@', end = '===',)
print('Take your cash {},remaining balance is:{}'.format(cash,typeValue))
print('your doing good')

a = 10
b = 20
c = a + b
print(a, b, c, sep= '->')
