
def wei(a,b):
    def nei(x):
        print('y=%d*%d+%d'%(a,x,b))
        y=a*x+b    #因为ab值只是进行运算，所以不需要声明nonlocal
        return y
    return nei
a=wei(2,3)
print(a(2))


