class DogCc(object):
     __isinstand=None
     def __init__(self):
         pass
     def __new__(cls):
         if cls.__isinstand == None:
             cls.__isinstand = object.__init__(cls)
         return cls.__isinstand
xiaoh=DogCc()
xiaog=DogCc()
print(id(xiaoh))
print(id(xiaog))


