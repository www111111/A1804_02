'''
#闭包
def test(out):
    def test_in(num_in):
        print(num_in)
        return num_in + out
    return test_in
a=test(1)#out=1  返回a=test_in
c=a(2)   #num_in=2 返回输出c
print(c)
#a=test(1)(2)
#print(a)
'''

#内部函数对外部函数作用域里变量的引用（非全局变量），则称内部函数为闭包。
def test(out=1):
    lis=[out]
    def test_in():
        lis[0]=lis[0]+1
        return (lis[0])
    return test_in
a=test()   #第一次调用test
print(a()) #2
print(a()) #3

b=test()   #又第一次调用test
print(b()) #2
print(b()) #3
print(b()) #4
print(b()) #5







