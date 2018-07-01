class FatherCc(object):
    __isinstand=None
    def __init__(self):
        self.name='zhangsan'
        print('初始化函数')
    def __str__(self):
        print('name is %s'%self.name)
    def __del__(self):
        print('程序执行完毕')
    def __new__(cls):
        print('new函数')
        if cls.__isinstand==None:
            cls.__isinstand=object.__new__(cls)
        return  cls.__isinstand
class sonCc(FatherCc):
    def __init__(self):
        FatherCc.__init__(self)
    def printStr(self):
        FatherCc.__str__(self)
xiaogang=sonCc()
xiaogang.printStr()
















