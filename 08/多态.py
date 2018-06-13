class Duck(object):
    def walk(self):
        print('鸭子在走')
    def swim(self):
        print('鸭子游泳了')

class People(object):
    def walk(self):
        print('老王在走')
    def swim(self):
        print('老王在游泳')

def Fun(n):#多态，n选择对象
    n.walk()#执行时才知道运行的哪个对象
    n.swim()

duck=Duck()
laow=People()
Fun(duck)#选择运行哪个对象
Fun(laow)















