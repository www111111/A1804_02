
def add(a,b):
    return a+b



print(__name__)#在内部调用__main__ 外部是一个路径。
if __name__== '__main__':#当输出为__main__的时候，说明在函数内部调用
    xx=add(6,6)#main则执行  以下，不为main不执行
    print('reult:%d'%xx)#不加判断。外调函数会把此部分输出

