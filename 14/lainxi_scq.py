'''
def f(c):
    lis=[x for x in range(1,c+1,2)]
    for a in lis:
        yield a
a=f(10)
print(next(a))
for i in a:
    print(i)
'''

lis=(x for x in range(1,101) if x%2!=0)#()小括号生成器
print(next(lis))
for i in lis:
    print(i)











