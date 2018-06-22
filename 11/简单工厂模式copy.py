class CarStore(object):#汽车类
    def createCar(self,typeName):
        pass
    def order(self,typeName):
        self.car=self.createCar(typeName)#对象.方法
        self.car.move()
        self.car.stop()

class Xiandai(CarStore):#4s店

    def createCar(self,typeName):
        self.CarFactory=CarFactory()#创建对象方式,为了创建不同对象
        return self.CarFactory.createCar(typeName)

class yilante(object):
    def move(self):
        print('伊兰特 moving')
    def stop(self):
        print('伊兰特 stoping')

class suonata(object):
    def move(self):
        print('索纳塔 moving')
    def stop(self):
        print('索纳塔 stoping')

class CarFactory(object):
    def createCar(self,typeName):
        if typeName=='伊兰特':
            self.car=yilante()
        elif typeName=='索纳塔':
            self.car=suonata()
        return self.car

suonataz=Xiandai()
suonataz.order('索纳塔')










