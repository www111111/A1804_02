class Car(object):
    __instance=None                         #用于保存实例化读对象
    __init_flag=False                       #表示一次都没执行的标志位
    def __init__(self,name):
        if Car.__init_flag == False:        #判断是否第一次执行
            self.name=name                  #如果第一次执行，进行赋值
            Car.__init_flag=True            #如果不是第一次执行就不执行，flag被True。
        #print(self.name)                   #在每次赋值以后进行输出显示12
    def __new__(cls,n):
        if cls.__instance==None:            #为了只创建一个内存所以判断是否第一次创建
            cls.__instance=object.__new__(cls)#执行一次就创建一个空间
        return cls.__instance
c1=Car('1')     #在内存只有一个空间，c1c2共用同个空间
c2=Car('2')
print(c1.name)#如果不进行初始化判断。输出最后执行的2,之前1被覆盖掉
print(c2.name)#进行初始化判断以后，最后输出1,因为执行了一遍，后来对象c2就不能给其name赋值
print(id(c1))
print(id(c2))























