print('=====Keyword argument ')
'''
def bottleDetails(name,color,capacity,height):
    print('name: {} color: {} capacity:{} height:{}'.format(name, color, capacity, height))
    
    
    
bottleDetails('water','Red', 100, 1.10)
bottleDetails('Red','water', 100, 1.10)
bottleDetails(height=100, capacity=1.10, name='water', color='Red')

'''
print('===variable number of arguments=======*args, **kwargs')
'''
def printAll(*numbers):
    for arg in numbers:
        print(arg)
        
printAll(1, 2, 5, 6, 8)
'''
'''
def multiply(*number):
    mul = 1
    for num in number:
        mul = mul * num
    return mul

result = multiply(1, 2, 3, 5, 5, 8)
print(result)
'''
'''
def multiply(start,*number):  #  becomes start  = 10
    mul = start
    for num in number:
        mul = mul * num
    return mul

result = multiply(10, 2, 3, 5, 5, 8)
print(result)
'''


def bottleDetails(**kwargs):
    for key, value in kwargs.items():
        print('{}:{}'.format(key, value))


bottleDetails(height=100, capacity=1.10, name='water', color='Red')

# passing *args, **kwargs from caller

def eatMe(apple,banana,grapes):
    print(apple, banana, grapes)
    
fruits = (10, 5, 21)
eatMe(*fruits)