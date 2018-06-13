
class A(object):
    def __init__(self):
        #self.name=name
        #print(self.name)
        print('init')
    def __del__(self):
        print('del')
    #def __new__(cls,*args,**kwargs):
    #    print('new')
    #    return object.__new__(cls)
    def __new__(cls):
        print('new')
        return object.__new__(cls)
a=A()
print(id(a))
b=A()
#print(A)
print(id(b))



























