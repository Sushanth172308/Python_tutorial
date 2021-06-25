print('Hello Rita')

a = 5
b = 10
c = 7

z = a + b * c
print(z)


a1, a2 = 5, 6

print(a1)

# Camel Case
userFullName = 'camel case'

# pascal Case
UserFullName = 'Pascal Case'

#Snake Case
user_full_name = 'Snake Case'

# another tutorial:

# program to calculate number of guides
a = 200
b = 100
c = 600
d = 40
a, b, c, d = 40, 40, 60, 50

total = a + b + c + d

#print(total)

oneGuideCost = 100

numberOfGuides = total / oneGuideCost

print(numberOfGuides)
'''
sum  = 10  #global spacce

def calculate():
    currentSum = 200
    totalSum = sum +currentSum
    print(totalSum)


calculate()
#print(currentSum)  # can't access
'''

sum = 50

def calculatee():
    global sum
    sum = sum + 20
    currentSum = 200
    totalSum = sum + currentSum
    print(totalSum)

calculatee()
print(sum)



