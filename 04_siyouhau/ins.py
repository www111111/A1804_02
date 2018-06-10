

class Animal:
    def __init__(self):
        self.__legs=4
        self.head=1
    def eat(self):
        print('吃')
    def get(self):
        return self.__legs

class Gou(Animal):
    def jiao(self):
        print('叫')

class Shapi(Gou):
    def drink(self):
        print('喝')
gou=Animal()
print(gou.get())
xgou=Gou()
print(xgou.get())
#print(xgou.__legs)












