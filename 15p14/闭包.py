def counter(start=0):   #初始值
    def iner():
        nonlocal start #访问外部函数的局部变量(python3)
        #在是声明之前用或者print 都会报警
        start +=1   #改变的时候加nonlocal  ！
        return start  #没返回变空
    return iner  #函数引用不是调用
a=counter(2)           #传参数，覆盖初始值
print(a())
print(a())

a=counter(2)           #在执行counter时只是定义了额iner  没有执行里面的内容
print(a())             #zineng只能a变量  或者 counter（2）（）

a=counter()
print(a())





