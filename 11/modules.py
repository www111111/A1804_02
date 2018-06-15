__all__=['b','c']#在from *的情况下，导入哪些函数的方法
def a():
    print('test1')
def b():
    print('test2')
def c():
    print('test3')

print(__name__)#是否在包外运行这个语句。如果内部则输出main则运行。
if __name__=='__main__':
    a()




