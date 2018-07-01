
class PeopleCc(object):
    def __init__(self,name):
        self.__name=name
    def setName(self,value):
        self.__name=value
    def getName(self):
        print('name is %s'%self.__name)

class ZhangsanCc(PeopleCc):
    def __init__(self):
        self.__money=0
    @property
    def money(self):
        print('money is %d' %self.__money)
    @money.setter
    def money(self,value):
        self.__money=value

cc=PeopleCc('xiaohuahua')
cc.setName('ligang')
cc.getName()

xg=ZhangsanCc()
xg.money=10
xg.money




