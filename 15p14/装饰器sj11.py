
def wai(i):
    def nei(name = '员工'):
        if name == '员工':
            i()
            print('errorname')
        else:
            print('errorname')
    return nei


def wai1(i):
    def nei1( paw ='123'):
        if paw == '123':
            i()
            print('errorpwd')
        else:
            print('errorpwd')
    return nei1



@wai           #装饰f1函数
def f1():
    print('f1')
@wai
@wai1
def f2():
    print('f2')
@wai
def f3():
    print('f3')
@wai
def f4():
    print('f4')

#f1('员工')
f2('员工')

'''
f3('员工1')
f4('员工1')
'''









