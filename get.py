'''
class Yl(object):
    def __init__(self,name):
        self.name=name
    def get(self):
        print(self.name)

    def set(self,name):
        self.name=name
        print(self.name)


yl1=Yl('yl')
yl1.get()
yl1.set('sb')
print(yl1.name)
'''



class Animal(object):
    def dong(self,a):
        print('111',a)

class Dog(Animal):
    def eat(self,a):
        #super().dong(a)
        self.dong(a)
        print('222')
ss=Animal()
dog=Dog()

dog.eat('bb')
ss.dong('s')
#引用带argument也可以用


