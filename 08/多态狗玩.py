class Dog(object):
    def game(self):
        return'普通狗简单的玩'

class XiaoTianDog(Dog):
    def game(self):
        return'啸天狗在天上玩'

class Person(object):
    def AndDogPlay(self,obj):
        print ('人在和',obj.game())#输出中不可加print（不区别print输出还是return）


dog=Dog()
xiaot=XiaoTianDog()
man=Person()
man.AndDogPlay(xiaot)#return返回符号等内容，输出不完美












