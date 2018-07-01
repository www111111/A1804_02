
def wai(i):

    def nei(name):
        if name == '员工':
            i()
        else:
            print('error')
    return nei

@wai           #装饰f1函数
def f1():
    print('f1')
@wai
def f2():
    print('f2')
@wai
def f3():
    print('f3')
@wai
def f4():
    print('f4')

f1('员工')
f2('员工')
f3('员工1')
f4('员工1')










