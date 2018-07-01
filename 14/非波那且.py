def f(day):
    n=0
    #a,b=0,1#数列赋值
    a=0
    b=1
    while n < day:
        yield(b)
        a,b=b,a+b
        n+=1
    return 'ok'
a=f(10)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
next(a)
for i in a:
    print(i)



















