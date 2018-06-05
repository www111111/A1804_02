import os

f=open('test.txt','r')
a=f.read()
f.seek(0,0)
for i in a:
    e=f.read(1)
    c=f.tell()
    print('con %s'%i)
    print('pos %s'%c)
    print(type(a))



