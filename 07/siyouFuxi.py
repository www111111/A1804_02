#子类的属性和父类属性相同，会执行子类本身的属性：重名
#属性，方法，私有化不可继承，不要重名
'''
class Father(object):
    def __init__(self):
        self.xing='王'
        self.height=180
    def kaice(self):
        print('开车。。。。')
    def __dubo(self):
        print('赌博')
class Son(Father):
    pass
大头儿子=Son()
print(大头儿子.xing)
大头儿子.kaice()
#大头儿子.__dubo()
大头儿子.xing='aaa'
print(大头儿子.xing)
大头儿子.height=190
print(大头儿子.height)
'''






class Father(object):
    def __init__(self,name,age):
        self.xing=name
        self.age=age
    def kaice(self):
        print('开车。。。。')
class Son(Father):
    def __init__(self,name,age):#重写
        #self.xing=name#重写
        #super().__init__(name)
        #Father.__init__(self,name)
        super(Son,self).__init__(name,age)
    def kaice(self):
        #print('保时捷')
        super().kaice()


大头儿子=Son('老王',22)
print(大头儿子.xing)
print(大头儿子.age)
大头儿子.kaice()










