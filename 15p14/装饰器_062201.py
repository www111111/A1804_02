'''
def wei(fun):   #形参
    def nei(a,b):
        print('jc ,agr= %d,%d'% (a,b))
        fun(a,b) #函数调用，传递实际参数
    return nei
@wei
def foo(a,b):
    print('foo,agr=%d,%d'%(a,b))

foo(1,2)
'''

#ctrr v I(shift i) #  shift v d  ctr i  zhuxiao
def wei(fun):   #形参
    def nei(*args):
        print('nei is ', args)
        fun(args) #函数调用，传递实际参数
    return nei
@wei
def foo(*args):
    print('foo agr is',args)

foo(1,2)
'''
def wei(fun):   #形参
    def nei(*args,**kwargs):
        print('nei is ', args)
        print('nei is ', kwargs)
        fun(*args,**kwargs) #函数调用，传递实际参数 args kwargs的时候相当于参数传到 foo(*args,**kwargs)。-->foo agr is ((1, 2), {'b': 1})  else  输出(1, 2) {'b': 1}
    return nei
@wei
def foo(*args,**kwargs):
    print('foo agr is',args)
    print('foo agr is',kwargs)

#foo(1,2,b=1)

'''


'''
def wei(fun):   #形参  篡改地函数的引用
    def nei(*args):  #传递函数需要的参数 shift v .
        print('jc ',*args)
        return(fun(*args)) #函数调用，传递实际参数

    return nei

@wei
def foo(*args):
    return ('foo',*args)
print(foo(1,2))
'''
'''
def zsq(a): #1在外层建立函数，名字和装饰器相同
    def wei(fun):   #形参  篡改地函数的引用
        def nei():  #传递函数需要的参数 shift v .
            print('jc' )
            print(a)
            return(fun()) #函数调用，传递实际参数
        return nei
    return wei  #2返回函数

@zsq(123)  #3装饰器赋值123
def foo():
    return ('foo')
print(foo())

'''


















