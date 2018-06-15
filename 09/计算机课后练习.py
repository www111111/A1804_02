
class Jisuanji(object):
    __instance=None
    __flag=False
    def __init__(self,name):
        if Jisuanji.__flag == False:
            self.name=name
            Jisuanji.__flag=True
    def __new__(cls,k):#单例
        if cls.__instance==None:
            cls.__instance=object.__new__(cls)
        return cls.__instance
    def add(self,a,b):
        return a+b
    def min(self,a,b):
        return a-b
    def mul(self,a,b):
        return a*b
    def div(self,a,b):
        return a/b

class JdCala(Jisuanji):
    def js(self,a,b,c):
        if c=='+':
            return super().add(a,b)
        if c=='-':
            return super().min(a,b)
        if c=='*':
            return super().mul(a,b)
        if c=='/':
            return super().div(a,b)

class FzCala(Jisuanji):
    def js(self,a,b,c):
        if c=='+':
            e=super().add(a,b)
            a=e
            return e
        if c=='-':
            e=super().min(a,b)
            a=e
            return e
        if c=='*':
            e=super().mul(a,b)
            a=e
            return e
        if c=='/':
            e=super().div(a,b)
            a=e
            return e

jsq=JdCala('简单计算器')
#jsq_fz=FzCala('复杂计算器')

while True:
    a=int(input('num1'))
    b=input('symbol')
    c=int(input('num2'))
    print(jsq.js(a,c,b))
    #print(jsq.js(2,1,'-'))
'''

a=int(input('num1'))
while True:
    b=input('symbol')
    c=int(input('num2'))
    print(jsq_fz.js(a,c,b))
    #print(jsq.js(2,1,'-'))

'''





















'''
    def jis(self):#函数加在class运算的时候
        while True:
            try:
                a=int(input('a'))
                c=input('输入 + or - or * or /')
                b=int(input('b'))
                if c=='+':
                    print (a+b)
                elif c=='-':
                    print (a-b)
                elif c=='*':
                    print (a*b)
                elif c=='/':
                    print (a/b)
                d=int(input('1.继续运算 2.结束运算'))
                if d==2:
                    break
            except Exception as result:
                print('程序异常,原因是：%s'%result)

j=Jisuanji('计算器')
#b=Jisuanji('老虎机')
print(j.name)
#print(b.name)
j.jis()

'''





























