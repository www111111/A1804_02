'''
#type（类的）
# 元类  : 创建类   type
#1.type 创建 类
#  type(类的名称, (类继承对象),{属性})
Test1 = type('Test',(),{}) # 定了一个Test2类
t1=Test1()
print(Test1)
print(t1)


Test1 = type('Test',(),{'a':1,'b':2}) # 定了一个Test2类
t1=Test1()
print(Test1.a)
print(t1.a)
print(Test1.b)
print(t1.b)
'''

Test1 = type('Test',(),{'a':1,'b':2}) # 定了一个Test2类
print(Test1)
def aa(self):
    print('aa',self.b)

Test_child = type('Test',(Test1,),{'c':aa}) # 定了一个Test2类
t1=Test_child()
print('tt',t1)
print('tt',t1.a)
t1.c()
print(t1.c)













