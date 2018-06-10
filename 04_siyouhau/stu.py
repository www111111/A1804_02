import sys
class Stuclass:
    def __init__(self,name,sex,age):
        self.name=name
        self.sex=sex
        self.age=age
        self.cj={}

    def __str__(self):
        return 'name:'+self.name+'\n'+'age:'+self.age+'\n'+'sex:'+self.sex+'\n'+'cj'+str(self.cj)

    def write(self):
        f=open('1.txt','a')
        print(20*'*')
        f.write('name:'+self.name+'\n'+'age:'+self.age+'\n'+'sex:'+self.sex+'\n'+'cj'+str(self.cj))
        print(20*'*')
        f.close()

    def addlvcj(self,kemv,cengji):
        self.cj[kemv]=cengji


s1=Stuclass('s1','男','22')
s2=Stuclass('s2','女','22')
s3=Stuclass('s3','男','21')

def ren(a):
    for i in range(1,3):
        k=input('输入科目')
        v=input('输入成绩')
        a.addlvcj(k,v)

ren(s1)
print(s1)
s1.write()

ren(s2)
print(s2)
s2.write()

ren(s3)
print(s3)
s3.write()



#a=print(s1)
#print(a)


print(sys.getrefcount(s2))#ref链接
print(isinstance(s1,Stuclass))








