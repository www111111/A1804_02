

class Animal:
    import os  #open报错
    def __init__(self,name):
        self.__name=name
        self.f=open('name.txt','r')   #打开文件放此
    def __del__(self):#del找不到open
        print(111111111111111)
        self.f.write(self.__name)
        self.f.close()
    def set_name(self):
        f=open('name.txt','r')
        du=f.read()
        if len(du)>0:
            self.name=du
            f.close()
        else:
            print('xx')
            f.close()

    def get_name(self):
        self.__name=self.f.read()
        return(self.__name)
        f.close()
dog=Animal('小cat')
#print(dog.set_name())
print(dog.get_name())

'''
dog1=dog
#print('end')
del dog
del dog1
print('end')

'''
















