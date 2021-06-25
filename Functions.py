print('==========Function=====')
'''
# with out function
number1 = 19
number2 = 18
number3 = 22

if number1%2 ==0:
    print('{} is even'.format(number1))
else:
    print('{} is odd'.format(number1))

if number2 % 2 == 0:
    print('{} is even'.format(number2))
else:
    print('{} is odd'.format(number2))

if number3 % 2 == 0:
    print('{} is even'.format(number3))
else:
    print('{} is odd'.format(number3))

'''
# With using functions:
'''
def evenOrodd(number):
    'this function is for even or odd nunber check'
    if number % 2 == 0:
        print('{} is even'.format(number))
    else:
        print('{} is odd'.format(number))

evenOrodd(12)
evenOrodd(16)
evenOrodd(18)
evenOrodd(11)
evenOrodd(15)
evenOrodd(11)

print(evenOrodd.__doc__)
print(print.__doc__)
print(type.__doc__)

'''

def cubeOfAnumber(number):
    cube = number*number*number
    return cube

result = cubeOfAnumber(7)
print('result is ', result)

# pass by reference
def calculate(myMarks):
    myMarks[2] = 70

marks =[80, 98, 32, 70, 89]
calculate(marks)
print(marks)

def calculate(myMarks):
    myMarks = [70, 20, 50]

marks =[80, 98, 32, 70, 89]
calculate(marks)
print(marks)

# pass by refference
def luckyNuber(number):
    number = 20
    return number
number = 10
print(luckyNuber(number))
print(number)


# Default arguments:

def inAbox(x =110):
    print(x)
    return



print(inAbox())
print(inAbox(20))
