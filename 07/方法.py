class People(object):
    guoji='china'#类属性
    def __init__(self):
        self.name='小明'#实例化属性

    def get(self):#实例化方法
        return self.name
    @classmethod#修饰器
    def get_guoji(cls):
        return cls.guoji
    @classmethod
    def zgh(cls):
        print('中国话')#不用return


class Tool(object):
    @staticmethod
    def menu():
        print('*'*30)
        print('666')
        print('*'*30)
    @staticmethod
    def shuru(n):
        print(n,'制做')

Tool.menu()
Tool.shuru(1111)
lau=People()
print(People.guoji)
print(lau.guoji)
lau.guoji='usa'
print(People.guoji)
print(lau.guoji)
del lau.guoji
print(lau.guoji)

'''
xiaoming=People()#实例化对象
print(xiaoming.name)
xiaoming.get()
print(People.guoji)
print(People.get_guoji())
#People.get_guoji()
'''






















