
class Car(object):
    def __init__(self,carType):
        self.carType=carType
    def move(self):
        print('%s car moving。。。。。'%self.carType)
    def stop(self):
        print('%s car stop。。。。。'%self.carType)
    def Fun(self):
        self.move()
        self.stop()
class Car_Store(object):
    def order(self,typeName):
        a = Car(typeName)

        #super().Fun()
        a.Fun()
Yi=Car_Store()
Yi.order('伊兰特')
Yi.order('索纳塔')
Yi.order('mini')
Yi.order('现代')



























