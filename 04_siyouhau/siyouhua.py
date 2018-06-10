class People:
    ''' 私有化讲解'''
    def __init__(self,name,salary):
        self.__name=name
        self.salary=salary
    def get_name(self):
        return self.__name
    def set_name(self,n):
        self.__name=n
        return self.__name

    def __send_msg(self):
        print('验证码发送成功')
    def get_msg(self):
        self.__send_msg()

yl=People('于',10000)
print(yl.get_name())
#print(yl.__name)
#yl.__name='xx'
yl.set_name('666')
print(yl.get_name())
#yl.__send_msg()
yl.get_msg()

huahua=People('花花',1000)
huahua.get_msg()





class People:
    '''私有化理解 '''
    def __init__(self,name,yao):
        self.__name=name
        self.__yao=yao
    def get_yao(self,n):
        if n=='小花花':
            return self.__yao
        else:
            return 200
    def __sw(self):
        return '造哇成功'
    def jiehun(self,n):
        if n=='yl':
            print(self.__name+'结婚'+n+self.__sw())#self.__sw()值为返回值，输出报错.
xiaohua=People('小花花',22)
print(xiaohua.get_yao('小花花'))
xiaohua.jiehun('yl')













