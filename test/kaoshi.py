'''
dic={1:2}
print(bool(dic))
'''
'''
a=bool('abc' > 'xyz')
print(a)
'''
'''
dic={(1,2,3):'eeeeee'}
print(type(dic))
'''
'''
(2,3,4)[2]=5
'''
'''
l=[]
for i in range(3):
    a=int(input('xxx'))
    l.append(a)
    l.sort()
print(l)
'''
'''
#c=0
for i in range(1,10):
    for a in range(1,10):
        c=a*i
        print('%d*%d=%d '%(a,i,c),end='\n\t ')
'''
'''
import random
i=0
a=random.randint(1,100)
while True:
    b=int(input('ss'))
    i+=1
    if b>a:
        print('big')

    elif b<a:
        print('small')
    else:
        print('yes')
        break
print('caile %d'%i)
if(i<=5):
    print('lihai')
else:
    print('nl')
'''
'''
import random

b=random.randint(1,3)
a=int(input('sr'))

if(a==1 and b==2) or (a==2 and b==3) or (a==3 and b==1):
    print('wan win')
elif a==b:
    print('ping')

else:
    print('pc win')

'''

a=int(input('shur'))
if a%4==0 and a%100!=0 :
    print('run')
elif a%400==0:
    print('run')
else:
    print('ping')



