# Object --> Anything that has state and behavior is called object
# Laptop
#chair
#state  = lakshanalu ==properties =laptop, color, height, weight
# behavior = panulu ==work, open,close
# imp water bottle
# state = color,height,width,
#behavior = fill the water, put a cap to bottle,we can clean it


# Class
# class is a blueprint to create objects
'''
--water bottle:
Attributes/properties/State:
. Id
. Color
. Capacity
. Height
etc
Functions /Behavior
. Wash
. Set Cap
. Fill Water
etc
'''
'''
id = 1
color = 'red'
capacity = 1
height = 10

def wash():
    print('Washing')

def setCap():
    print('setCap')

def FillWater():
    print('filling water')
'''
print('---------------------------------------------------------------------')

class Bottle:
    'This class used to create a bottle and also lean about bottle usage'
    # Properties/states
    CompanyName = 'Distled Water Company'

    # Class level objects/static objects


    #id = 1
    #color = 'red'
    #capacity = 1
    #height = 10



    # Constructor

    def __init__(self, color, capacity):
        self.color = color
        self.capacity = capacity
        print('construction called')
     # destructor

    def __del__(self):
        pass
     #   print('destructor called')

    #Functions/Behavior

    def wash(self):
        print(self)
        print('Washing')

    def setCap():
        print('setCap')

    def FillWater():
        print('filling water')

# Object creation
print(Bottle.CompanyName)
bottle1 = Bottle('green',2)
bottle2 = Bottle('Yello', 5)
bottle3 = Bottle('blue', 6)
print(bottle1.CompanyName)
print(bottle1)
print(bottle1.color)
print(bottle1.wash())


print('===Constructior=====')
'Constructor gets called and initializes all the attributes/properties with default values' \
'All the properties and attributes will be placed in a memory loacation'
'Returns that memory location'

# Types of Constructors
'1. Default constructor'
'2. Constructor with parameters'

' Destructor  or garbage collector'
'When destroyed an object  '

print('****************Inheritance*******************')

class CopperBottle(Bottle):
    #Constructor of child class
    def __init__(self, make, model):
        ' To send data from child class to partent class via child constructor'
        'we can also use parents class or .super()'
        #Bottle.__init__(self, make, model)
        super().__init__(make, model)

        print('chiild constructor is calling')
    def morningWater():
        print('Morning is calliig')


print(CopperBottle.CompanyName)
#copper1 = CopperBottle('Green',5).. if we dont have child constrctor
copper1 = CopperBottle(1954, 'Leo')
copper1.wash()

'To know parent of any class we can use  class.__bases__'
print(Bottle.__bases__) # every class is derived from the object
print(CopperBottle.__bases__)
print(CopperBottle.__class__.__bases__)





