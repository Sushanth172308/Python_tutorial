print('====Yield, Generators=====')
# Yield suspends functions execution and sends value back to the caller and then
#resumes where it left off
'''
def coconutCapacity(number):
    colories = number*19
    return colories
    print('super')

calories = coconutCapacity(2)
print(calories) # comes from function
'''
'''
def coconutCapacity(number):
    colories = number*19
    yield colories
    print('super')

calories = coconutCapacity(2)
print(calories) # comes from function
# results generator object

'''

def coconutCapacity(number):
    colories = number*19
    yield colories
    print('super')

calories = coconutCapacity(2)
print(calories) # comes from function

for i in calories:
    print(i)
