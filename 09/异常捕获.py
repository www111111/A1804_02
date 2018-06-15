'''
try:
    print(sss)
    print('老铁双击')
    print(666)
    print('%d' %'qq')
except (NameError,TypeError) as rusult:
    print('程序异常 %s'%rusult)
else:
    print('程序正常')
'''
'''
file=input('file')
f=open(file,'w')
try:
    s=f.read()
    print(s)
except  Exception as result:            #返回错误结果，并存在变量里
    print('程序异常 原因是：%s'%result) #Exception 所有的错误
else:
    print('程序正常')

finally:                               #有无异常，执行完程序，最终走的
    f.close()
#捕捉到错误，不影响下面程序运行.

'''

try:
    print('name')
    try:
        for i in (11.1):
            print(i)
    except Exception as result:#在内层捕捉不到错误会让外面的去捕捉
        print(result)
except NameError as result:
    print('big %s'%result)











