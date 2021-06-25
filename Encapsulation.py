'capsol Example'
'Encapsulation is process of wrapping code and data together in to a single unit'
'Encapsulation prevents accidental modification of the data'
' by using Access Modifiers:Public, Protected, privatec-- we can achieve Encapsulation'

'Public'
'Protected---> use _ before the variable'
'Private   >  we can access only within the class -use __ before the variable'

class Bottle:
    'This class used to create a bottle and also lean about bottle usage'
    # Properties/states
    CompanyName = 'Distled Water Company'

    def __init__(self, color, capacity, height):
        self._color = color # here ._color is protected variable
        self.capacity = capacity # here capacity is public variable
        self.__height = height# Here __height is private variable
        print('construction called')
     # destructor

    def __del__(self):
        pass
     #   print('destructor called')

    #Functions/Behavior

    def wash(self):
        print(self)
        print('Washing', self._color, self.__height)

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
#print(bottle1.color)
print(bottle1.wash())
print(bottle1.__height)

class CopperBottle(Bottle):
    #Constructor of child class
    def __init__(self, make, model):
        ' To send data from child class to partent class via child constructor'
        'we can also use parents class or .super()'
        Bottle.__init__(self, make, model)

    def morningWater(self):
        print('Morning is calliig', self._color)
        #print('Morning is calliig', self.__height)