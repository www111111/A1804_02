
def f1():
    print('f1')
def f2():
    print('f2')
def f3():
    print('f3')
def f4():
    print('f4')

def wai(i):

    def nei(name):
        if name == '员工':
            i()
        else:
            print('error')
    return nei


def main():
    fun = input('输入部门,f1/f2/f3/f4\n\t')
    fun1 = input('输入职位\n\t')
    if fun == 'f1':
        a=wai(f1)
        a(fun1)
    elif fun == 'f2':
        a=wai(f2)
        a(fun1)
    elif fun == 'f3':
        a=wai(f3)
        a(fun1)
    elif fun == 'f4':
        a=wai(f4)
        a(fun1)
if __name__ == '__main__':
    main()










