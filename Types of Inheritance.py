'Multiple inheritance--> 2 or more parents  ---- to child '
class Class1:
    def join(self):
        print('joined  mehtod from Class1 is calling')

class Class2:
    def subscribe(self):
        print('subscribe method from Class2 is calling')

class Class3(Class1, Class2):
    def comment(self):
        print('Calling comment method from Class3')

cls3 = Class3()
cls3.subscribe()
cls3.join()
cls3.comment()


'Multilevel inheritance --> parent-child-grandchild'

class Class1:
    def join(self):
        print('joined  mehtod from Class1 is calling')

class Class2(Class1):
    def subscribe(self):
        print('subscribe method from Class2 is calling')

class Class3(class2):
    def comment(self):
        print('Calling comment method from Class3')

cls3 = Class3()
cls3.subscribe()
cls3.join()
cls3.comment()

'Hierarchical Inheritance - > one parent --> more childs '

class Class1:
    def join(self):
        print('joined  mehtod from Class1 is calling')

class Class2(Class1):
    def subscribe(self):
        print('subscribe method from Class2 is calling')

class Class3(class1):
    def comment(self):
        print('Calling comment method from Class3')

class Class4(class1):
    def details(self):
        print('Calling detils method from Class4')

'Hybrid Inheritance--> Combination of (single, multiple,multilvel, hierarchical)'