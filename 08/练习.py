class Car(object):
    def __init__(self,name):
        self.car=name
    def run(self):
        return('汽车在飞奔')

class Vw(Car):#init执行父类初始化auto?
    def __init__(self,name):
        super().__init__(name)
    def run(self):
        return(self.car+'汽车在飞奔')

class Bwm(Car):
    def run(self):
        return(self.car+'汽车在飞奔')


class Mb(Car):
    def run(self):
        return('奔驰汽车在飞奔')


class People(object):
    def __init__(self):
        self.name='老王'
    def drive(self,n):
        print(self.name,'开着',n.run(),'去泡妞')

type=input('type')
car1=Car('大众')
man=People()
vw=Vw(type)
man.drive(vw)
'''
vw=Vw('大众cc')
man.drive(vw)
bwm=Bwm('宝马迷你')
man.drive(bwm)
bwm=Bwm('宝马x6')
man.drive(bwm)
mb=Mb('奔驰')
man.drive(mb)
'''















