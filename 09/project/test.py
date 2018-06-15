
a=(1)
b=(1,)
print(type(a),type(b))
#int型


x=1
y=2
print(x,y)
a = x
b = y
x = b
y = a
print(x,y)


b=lambda x,y=5:x+y
print(b(1,7))
#传递参数value优先于缺省值

import random


l=[]
c=0
while len(l)<5:
    if len(l)<5:
        a=random.randint(1,5)
        l.append(a)
        ff=l[c]
        c+=1

        if l.count(ff)>1:
            l.remove(ff)
            c-=1
print(l)
y=0
print('qqqqqqqqq')
ss=random.sample(range(6),6)
for i in ss:
    y=i+y
print(y)
print(ss)









print(20*'*')
def g(k):
    h=k+2
    return k
    return h
print(g(2))
#返回第一个值
